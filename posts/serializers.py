from rest_framework import serializers

from .models import Tag, Post, Comment
from equipment.serializers import CameraSerializer, FilmSerializer, LensSerializer


class TagSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Tag
        fields = ['id', 'name']


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.user.username')
    post = serializers.ReadOnlyField(source='post.id')

    class Meta:
        model = Comment
        fields = [
            'id',
            'author',
            'post',
            'text',
            'posted_on',
        ]


class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.user.username')
    tags = TagSerializer(many=True)
    camera = CameraSerializer()
    film = FilmSerializer()
    lens = LensSerializer()
    comments = CommentSerializer(many=True)
    # comments = serializers.PrimaryKeyRelatedField(many=True, queryset=Comment.objects.all())

    class Meta:
        model = Post
        fields = [
            'id',
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
