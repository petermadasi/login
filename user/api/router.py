# App
from user.api.viewsets import ProfileViewSet

from rest_framework import routers

router = routers.SimpleRouter()
router.register(
    r'profile',
    ProfileViewSet,
    basename='profile'
)