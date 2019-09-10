from rest_framework import serializers

from .models import Tag, Post, Comment
from users.serializers import UserProfileSerializer
from equipment.serializers import CameraSerializer, FilmSerializer, LensSerializer


class TagSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Tag
        fields = ['name']


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    author = UserProfileSerializer()
    # post = PostSerializer()

    class Meta:
        model = Comment
        fields = [
            'author',
            # 'post',
            'text',
            'posted_on',
        ]


class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = UserProfileSerializer()
    tags = TagSerializer(many=True)
    camera = CameraSerializer()
    film = FilmSerializer()
    lens = LensSerializer()
    comments = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = [
            'author',
            'title',
            'caption',
            'taken_on',
            'posted_on',
            'tags',
            'camera',
            'film',
            'lens',
            'aperture',
            'shutter_speed',
            'exposure',
            'comments',
        ]
