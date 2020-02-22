from django.shortcuts import render
from .models import modeltemp

def agencyHome(request):
    context = {} 
    return render(request, 'myapp/agencyhome.html', context)



# this is for the about page
# def demoabout(request):
#     context = {}
#     return render(request, 'myapp/demoabout.html', context)
