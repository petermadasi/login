# App
from user.api.serializer import ProfileSerializer
from user.models import UserProfile

# Third Party
from rest_framework import viewsets

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer