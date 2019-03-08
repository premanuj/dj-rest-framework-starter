from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .serializer import UserSerializer
from rest_framework.response import Response
from rest_framework import generics


# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)


class UserRegistration(generics.CreateAPIView):
    serializer_class = UserSerializer

