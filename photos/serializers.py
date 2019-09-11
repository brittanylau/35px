from rest_framework import serializers

from .models import Tag, Photo, Comment, Image
from equipment.models import Brand, Camera, Film, Lens
from equipment.serializers import (
    CameraSerializer,
    FilmSerializer,
    LensSerializer
)


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"


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

    # comments = CommentSerializer(many=True)

    class Meta:
        model = Photo
        fields = [
            'id',
            'url',
            'author',
            'title',
            'caption',
            'posted_on',
            'tags',    # must be existing
            'camera',  # must be existing
            'film',    # must be existing
            'lens',    # must be existing
            'aperture',
            'shutter_speed',
            'exposure',
            # 'comments',
        ]

    def create(self, validated_data):
        tag_data = validated_data.pop('tags')
        camera_data = validated_data.pop('camera')
        film_data = validated_data.pop('film')
        lens_data = validated_data.pop('lens')

        camera = Camera.objects.get(
            brand=Brand.objects.get(name=camera_data['brand']['name']),
            name=camera_data['name'],
        )
        film = Film.objects.get(
            brand=Brand.objects.get(name=film_data['brand']['name']),
            name=film_data['name'],
        )
        lens = Lens.objects.get(
            brand=Brand.objects.get(name=lens_data['brand']['name']),
            name=lens_data['name'],
        )

        photo = Photo.objects.create(
            **validated_data,
            camera=camera,
            film=film,
            lens=lens
        )

        for data in tag_data:
            tag_name = data['name']
            tag = Tag.objects.get(name=tag_name)
            photo.tags.add(tag)

        return photo
