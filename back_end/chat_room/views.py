from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import generics
from django.contrib.auth.models import User
from chat_room.models import Room
from chat_room.serializers import (RoomSerializers, UserSerializer)


class Rooms(APIView):
    #permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        rooms = Room.objects.filter(Q(creator=request.user) | Q(invited=request.user) | Q(private=False))
        serializer = RoomSerializers(rooms, many=True)
        return Response(serializer.data)

    def post(self, request):
        name = request.data.get("name")
        private = request.data.get("private")
        try:    
            Room.objects.create(creator=request.user, name=name, private=private)
            return Response(status=201)
        except:
            return Response(status=400)

    def delete(self, request):
        room_req = request.data.get("id")
        creator = request.user
        room = Room.objects.get(id=room_req)
        if room.creator == creator:
            room.delete()
            return Response(status=204)
        else:
            return Response(status=400)


class AddUsersRoom(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        room_req = request.data.get("id")
        user_req = request.data.get("user")
        user_id = user_req.get("id")
        user = User.objects.get(id=user_id)
        creator = request.user
        room = Room.objects.get(id=room_req)
        if room.creator == creator:
            room.invited.add(user)
            room.save()
            return Response(status=201)
        else:
            return Response(status=400)

    def delete(self, request):
        room_req = request.data.get("id")
        user_req = request.data.get("user")
        user_id = user_req.get("id")
        user = User.objects.get(id=user_id)
        creator = request.user
        room = Room.objects.get(id=room_req)
        if room.creator == creator:
            room.invited.remove(user)
            room.save()
            return Response(status=204)
        else:
            return Response(status=400)

