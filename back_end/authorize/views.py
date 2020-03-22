from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from authorize.serializers import *
#from authorize.models import *

# Create your views here.
class CreateUser(generics.CreateAPIView):
    serializer_class = CreateUserSerializers


class UserList(APIView):
    def get(self, request):
        alluser = User.objects.all()
        serializer = UserListSerializers(alluser, many=True)
        return Response({"data": serializer.data})

        