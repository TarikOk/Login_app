from django.contrib.auth.models import User
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
#from authorize.models import *


class CreateUserSerializers(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('username', 'email', 'password')

class UserListSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'date_joined')
