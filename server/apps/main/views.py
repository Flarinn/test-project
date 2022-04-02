from django.contrib.auth import get_user_model
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import AbstractUser
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from server.apps.main.models import UserProfile, Password, Category
from server.apps.main.serializer import UserSerializer, UserprofileSerializer, PasswordSerializer, \
    CategorySerializer

User = get_user_model()


class UserViewSet(ModelViewSet):
    """API для работы с пользователями."""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserprofileView(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserprofileSerializer
    permission_classes = [IsAuthenticated]


class PasswordView(generics.CreateAPIView):
    queryset = Password.objects.all()
    serializer_class = PasswordSerializer
    permission_classes = [IsAuthenticated]


class CategoryView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
