from django.shortcuts import render
from rest_framework import viewsets
from .models import UserProfile
from user.serializer import UserSerializer

class UserProfileView(viewsets.ModelViewSet):
    queryset=UserProfile.objects.all()
    serializer_class=UserSerializer
    

# Create your views here.
