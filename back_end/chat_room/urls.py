from django.urls import path
from chat_room.views import *
#from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('rooms/', Rooms.as_view()),
    path('rooms/<str:pk>/', RoomDetail.as_view()),
    path('rooms/invite/', AddUsersRoom.as_view()),
]

#urlpatterns = format_suffix_patterns(urlpatterns)