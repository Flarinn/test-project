from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import UserProfile, Password, Category
from django.contrib.auth.models import AbstractUser

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]


class UserprofileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["profilepic"]


class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Password
        fields = ["comment", "url", "encrypted_password", "device", "category"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
