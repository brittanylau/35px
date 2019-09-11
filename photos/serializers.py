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


class PhotoNameSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='photos:photo-detail-api'
    )

    class Meta:
        model = Photo
        fields = [
            'url',
            'title',
        ]


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='photos:comment-detail-api'
    )
    author = serializers.ReadOnlyField(source='author.user.username')
    photo = PhotoNameSerializer()

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

    def create(self, validated_data):
        photo_data = validated_data.pop('photo')
        photo = Photo.objects.get(title=photo_data['title'])  # ideally use ID but not sure how
        comment = Comment.objects.create(**validated_data, photo=photo)
        return comment

    # TODO: update method


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

    class Meta:
        model = Photo
        fields = [
            'id',
            'url',
            'author',
            'title',
            'caption',
            # 'taken_on',
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

    def create(self, validated_data):
        print('hi')
