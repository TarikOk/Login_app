from django.db.models import Q
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from django.contrib.auth.models import User
from chat_room.models import Room
from chat_room.serializers import (UserSerializer, RoomSerializers)


class Rooms(APIView):
    #permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        rooms = Room.objects.filter(Q(creator=request.user) | Q(invited=request.user) | Q(private=False))
        serializer = RoomSerializers(rooms, many=True)
        return Response(serializer.data)

    def post(self, request):
        name = request.data.get("name")
        private = request.data.get("private")
        user_id = request.data.get("invited")
        try:
            Room.objects.create(creator=request.user, name=name, private=private)
            users = user_id.get("id")
            for user in users:
                user = User.objects.get(id=user)
                creator = request.user
                room = Room.objects.get(id=room_req)
                if room.creator == creator:
                    room.invited.add(user)
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


class RoomDetail(APIView):

    def get_object(self, pk):
        try:
            return Room.objects.get(hash_id=pk)
        except Room.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        room = self.get_object(pk)
        serializer = RoomSerializers(room)
        return Response(serializer.data)
    

class AddUsersRoom(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        room_req = request.data.get("id")
        user_id = request.data.get("invited")
        users = user_id.get("id")
        for user in users:
            user = User.objects.get(id=user)
            creator = request.user
            room = Room.objects.get(id=room_req)
            if room.creator == creator:
                room.invited.add(user)
            else:
                return Response(status=400)
        room.save()
        return Response(status=201)

    def delete(self, request):
        room_req = request.data.get("id")
        user_id = request.data.get("invited")
        users = user_id.get("id")
        for user in users:
            user = User.objects.get(id=user)
            creator = request.user
            room = Room.objects.get(id=room_req)
            if room.creator == creator:
                room.invited.remove(user)
            else:
                return Response(status=400)
        room.save()
        return Response(status=204)
        