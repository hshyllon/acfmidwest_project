from django.shortcuts import render
from django.http import HttpResponse
from events.models import Event
#import datetime
from .extras import get_valid_upcoming_events
from .models import Volunteer, Album, Photo
from news.models import Blog


# Create your views here.
def index(request):
    getNum_events=Event.objects.filter(is_published = True).count()
    # if count greater than 3. Then get only latest three upcoming events
    if getNum_events > 3:
        get_events = Event.objects.filter(is_published = True).order_by('start_day')[:3]
    else:
        get_events = Event.objects.filter(is_published = True).order_by('start_day')
        # Get valid events 
    valid_events = get_valid_upcoming_events(get_events)
    try:
        latest_news = Blog.objects.filter(is_published = True).order_by('-create_date')[0]
        second_to_fourth_news = Blog.objects.filter(is_published = True).order_by('-create_date')[1:4]
    except:
        latest_news = ""
        second_to_fourth_news = ""
    context = {
        'valid_events' : valid_events,
        'latest_news' : latest_news,
        'other_news' : second_to_fourth_news,
        }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')

def history(request):
    return render(request, 'pages/history.html')

def team(request):
    return render(request, 'pages/team.html')

def volunteer(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        occupation = request.POST['occupation']
        message = request.POST['message']
        #print("trying")
        
        volunteer = Volunteer(fullname=fullname, email=email, phone=phone, address=address, occupation=occupation, message=message )
        volunteer.save()
        context = {
            "message" : "Your submission to volunteer has been received. We will reach back to you shortly. Thank you!",
            }
        return render(request, 'news/submission.html', context)
    else:
         
        return render(request, 'pages/volunteer.html')

def gallery(request):
    get_album = Album.objects.filter(is_published = True).order_by("create_date")
    get_album_cover = Photo.objects.filter(album_cover = True)
    print(get_album)
    print(get_album_cover)
    context = {
        'get_album' : get_album,
        'get_album_cover' : get_album_cover,
        }
    return render(request, 'pages/gallery.html', context)

def photo(request, album_id):
    get_album_images = Photo.objects.filter(photo_album = album_id).order_by("create_date")
    album = Album.objects.get(id = album_id)
    
    context = {
        'get_album_images' : get_album_images,
        'album' : album.album_title,
        }
    
    return render(request, 'pages/photo.html', context)


