from django.urls import include
from django.urls import path
from django.contrib.auth.views import LoginView
from .views import *

urlpatterns = [
    path('registration/', CreateUser.as_view()),
    path('userlist/', UserList.as_view()),
]