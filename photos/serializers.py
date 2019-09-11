from rest_framework import serializers

from .models import Tag, Photo, Comment
from equipment.serializers import (
    CameraSerializer,
    FilmSerializer,
    LensSerializer
)


class TagSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='photos:tag-detail-api'
    )

    class Meta:
        model = Tag
        fields = [
            'id',
            'url',
            'name'
        ]


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='photos:comment-detail-api'
    )
    author = serializers.ReadOnlyField(source='author.user.username')
    photo = serializers.ReadOnlyField(source='photo.id')

    class Meta:
        model = Comment
        fields = [
            'id',
            'url',
            'author',
            'photo',
            'text',
            'posted_on',
        ]


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='photos:photo-detail-api'
    )
    author = serializers.ReadOnlyField(source='author.user.username')
    tags = TagSerializer(many=True)
    camera = CameraSerializer()
    film = FilmSerializer()
    lens = LensSerializer()

    comments = CommentSerializer(many=True)
    # comments = serializers.PrimaryKeyRelatedField(
    #    many=True, queryset=Comment.objects.all()
    # )

    class Meta:
        model = Photo
        fields = [
            'id',
            'url',
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
