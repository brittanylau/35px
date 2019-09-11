from rest_framework import serializers

from .models import User, UserProfile
from photos.models import Post, Comment


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='users:user-detail-api'
    )

    class Meta:
        model = User
        fields = [
            'id',
            'url',
            'username',
            'is_staff',
        ]


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='users:profile-detail-api'
    )
    user = UserSerializer()
    photos = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Post.objects.all()
    )
    comments = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Comment.objects.all()
    )

    class Meta:
        model = UserProfile
        fields = [
            'id',
            'url',
            'user',
            'photos',
            'comments'
        ]
