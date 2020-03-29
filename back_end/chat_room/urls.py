# coding=utf-8
from django.urls import path
from chat_room.views import *

urlpatterns = [
    path('rooms/', Rooms.as_view()),
    path('room/invite', AddUsersRoom.as_view()),
]
