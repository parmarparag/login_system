from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('home/',home,name='home'),
    path('login/',loginpage,name='loginpage'),
    path('',signuppage,name='signuppage',),
    path('logout/',logoutpage,name='logout')
    
]
