from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contactus/',views.contactus,name='travel_contactus'),
    path('login/',views.logins,name='travel_login'),
    path('signup/',views.signup,name='travel_signup'),
    path('saveContactus/',views.saveContactus,name='travel_saveContactus'),
    path('savesignup/',views.savesignup,name='travel_savesignup'),
    path('savelogin/',views.savelogin,name='travel_savelogin'),
]