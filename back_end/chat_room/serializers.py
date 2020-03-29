from rest_framework import serializers
from django.contrib.auth.models import User
from chat_room.models import Room


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")


class RoomSerializers(serializers.ModelSerializer):
    creator = UserSerializer()
    invited = UserSerializer(many=True)

    class Meta:
        model = Room
        fields = ("id", "name", "creator", "invited", "date", "private")

