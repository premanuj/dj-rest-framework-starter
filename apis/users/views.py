from rest_framework import generics
from .serializer import UserSerializer
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.auth import authenticate

# Create your views here.


class UserCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()

    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


class LoginView(APIView):
    permission_classes = ()

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)
