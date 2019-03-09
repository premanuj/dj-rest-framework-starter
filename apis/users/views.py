from rest_framework import generics
from .serializer import UserSerializer, UserLoginSerializer
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt import views as jwt_views
from rest_framework.permissions import AllowAny

# Create your views here.


class UserCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


class LoginView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def get_serializer(self):
        return UserLoginSerializer()

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
