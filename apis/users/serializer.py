from django.db.models import Q
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.core.exceptions import ValidationError


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User(email=validated_data["email"], username=validated_data["username"])
        user.set_password(validated_data["password"])
        user.save()
        Token.objects.create(user=user)
        return user


class UserLoginSerializer(serializers.ModelSerializer):
    token = serializers.CharField(allow_blank=True, read_only=True)
    username = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ("username", "email", "password", "token")
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        email = data.get("email")
        username = data.get("username")
        password = data["password"]
        if not email and not username:
            raise ValidationError("Username or email is required to lofin")
        user = User.objects.filter(Q(email=email) | Q(username=username)).distinct()
        user = user.exclude(email__isnull=True).exclude(email__iexact="")
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("Email/Username is not valid.")

        if user_obj and not user_obj.check_password(password):
            raise ValidationError("Incorrect password.")
        data["token"] = "this is a token"

        return data
