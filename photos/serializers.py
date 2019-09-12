from rest_framework import serializers

from .models import Tag, Photo, Comment
from equipment.models import Brand, Camera, Film, Lens
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
        # TODO: Assert that photo exists and reference by id
        photo = Photo.objects.get(title=photo_data['title'])
        comment = Comment.objects.create(**validated_data, photo=photo)
        return comment

    # TODO: update method


class PhotoFileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = ['image']


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='photos:photo-detail-api'
    )
    author = serializers.ReadOnlyField(source='author.user.username')
    tags = TagSerializer(many=True)
    camera = CameraSerializer()
    film = FilmSerializer()
    lens = LensSerializer()
    image = serializers.StringRelatedField()

    # comments = CommentSerializer(many=True)

    class Meta:
        model = Photo
        fields = [
            'id',
            'url',
            'author',
            'image',
            'title',
            'caption',
            'posted_on',
            'tags',
            'camera',
            'film',
            'lens',
            'aperture',
            'shutter_speed',
            'exposure',
            # 'comments',
        ]

    def create(self, validated_data):
        camera_data = validated_data.pop('camera')
        film_data = validated_data.pop('film')
        lens_data = validated_data.pop('lens')
        tag_data = validated_data.pop('tags')

        camera_brand, created = Brand.objects.get_or_create(
            name=camera_data['brand']['name']
        )
        camera, created = Camera.objects.get_or_create(
            brand=camera_brand,
            name=camera_data['name'],
        )

        film_brand, created = Brand.objects.get_or_create(
            name=film_data['brand']['name']
        )
        film, created = Film.objects.get_or_create(
            brand=film_brand,
            name=film_data['name'],
        )

        lens_brand, created = Brand.objects.get_or_create(
            name=lens_data['brand']['name']
        )
        lens, created = Lens.objects.get_or_create(
            brand=lens_brand,
            name=lens_data['name'],
        )

        photo = Photo.objects.create(
            **validated_data,
            camera=camera,
            film=film,
            lens=lens
        )

        for t in tag_data:
            tag, created = Tag.objects.get_or_create(name=t['name'])
            photo.tags.add(tag)

        return photo

    def update(self, instance, validated_data):
        camera_data = validated_data.pop('camera')
        film_data = validated_data.pop('film')
        lens_data = validated_data.pop('lens')
        tag_data = validated_data.pop('tags')

        camera_brand, created = Brand.objects.get_or_create(
            name=camera_data['brand']['name']
        )
        camera, created = Camera.objects.get_or_create(
            brand=camera_brand,
            name=camera_data['name'],
        )

        film_brand, created = Brand.objects.get_or_create(
            name=film_data['brand']['name']
        )
        film, created = Film.objects.get_or_create(
            brand=film_brand,
            name=film_data['name'],
        )

        lens_brand, created = Brand.objects.get_or_create(
            name=lens_data['brand']['name']
        )
        lens, created = Lens.objects.get_or_create(
            brand=lens_brand,
            name=lens_data['name'],
        )

        instance.camera = camera
        instance.film = film
        instance.lens = lens

        instance.save()

        instance.tags.clear()

        for t in tag_data:
            tag, created = Tag.objects.get_or_create(name=t['name'])
            instance.tags.add(tag)

        return instance
