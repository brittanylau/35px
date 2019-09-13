from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import User, UserProfile
from ..serializers import UserSerializer, UserProfileSerializer


class UserViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileViewSet(ReadOnlyModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
