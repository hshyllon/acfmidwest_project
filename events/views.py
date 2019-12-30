from django.shortcuts import render
from .models import Event
from pages.extras import get_valid_upcoming_events
from django.shortcuts import get_object_or_404
# Create your views here.

def events(request):
    # get number of upcoming events
    getNum_events=Event.objects.filter(is_published = True).count()
    
    get_events = Event.objects.filter(is_published = True).order_by('start_day')
        # Get valid events 
    valid_events = get_valid_upcoming_events(get_events)
    context = {
        'valid_events' : valid_events,
        'number_of_events' : getNum_events,
        }
    return render(request, 'events/events.html', context)

def event(request, event_id):
    event_detail = get_object_or_404 (Event, pk = event_id)
    
    context = {
    'event_detail' : event_detail,
        }
    return render(request, 'events/event.html', context)
