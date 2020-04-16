from django.urls import path
from . import views


urlpatterns = [
    path('', views.agencyHome, name='home'),
    path('about', views.aboutUs, name='about'),
    path('contact', views.contactUs, name='contact'),
    path('services', views.services, name='services'),
#     path('demoaboutus', views.demoabout, name='demoabout'),
]
