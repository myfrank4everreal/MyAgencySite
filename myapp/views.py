from django.shortcuts import render
from .models import modeltemp
from django.core.mail import send_mail

def agencyHome(request):
    context = {} 
    return render(request, 'myapp/agencyhome.html', context)


def aboutUs(request):
    context = {} 
    return render(request, 'myapp/aboutus.html', context)


def contactUs(request):
    if request.method == "POST":
        message_phone = request.POST['phone']
        message_name  = request.POST['name']
        message_email  = request.POST['email']
        message = request.POST['message']
        
        



        send_mail(
            message,  
            message_phone,      
            message_email, 
            message_name,

            
            
            ['franklin.okolie4@gmail.com']
            )
            

       



        return render(request, 'myapp/contactus.html', {'message_name':message_name})
    else:
        return render(request, 'myapp/contactus.html', {})


def services(request):
    context = {} 
    return render(request, 'myapp/services.html', context)


# this is for the about page
# def demoabout(request):
#     context = {}
#     return render(request, 'myapp/demoabout.html', context)
