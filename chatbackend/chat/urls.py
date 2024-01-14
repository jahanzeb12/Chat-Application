from django.contrib import admin
from django.urls import path,include
from .views import create_room_with_users

urlpatterns = [
   path('create_room/', create_room_with_users, name='create_room_with_users'),

]