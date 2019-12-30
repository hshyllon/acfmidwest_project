from django.shortcuts import render
from .models import Contact
# Create your views here.


def contact(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        #print("trying")
        
        contact = Contact(fullname=fullname, email=email, phone=phone,message=message )
        contact.save()
        context = {
            "message" : "Your submission to contact us has been received. We will reach back to you shortly. Thank you!",
            }
        return render(request, 'news/submission.html', context)
    else:
         
        return render(request, 'contact/contact.html')

