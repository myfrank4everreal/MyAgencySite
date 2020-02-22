from django.urls import path
from . import views


urlpatterns = [
    path('', views.agencyHome, name='home'),
#     path('demoaboutus', views.demoabout, name='demoabout'),
]
