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
        photo = Photo.objects.get(title=photo_data['title'])  # ideally use ID but not sure how
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

        for t in tag_data:
            tag = Tag.objects.get(name=t['name'])
            photo.tags.add(tag)

        return photo

    def update(self, instance, validated_data):
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

        instance.camera = camera
        instance.film = film
        instance.lens = lens

        instance.save()

        keep_tags = []

        for t in tag_data:
            # if 'name' in t.keys():
            #     if Tag.objects.filter(name=t['name']).exists():
            #         tag = Tag.objects.get(name=t['name'])
            #         keep_tags.append(tag.id)
            # else:
            #     tag = Tag.objects.create(**t)
                tag = Tag.objects.get(name=t['name'])
                keep_tags.append(tag)

        for t in instance.tags.all():
            if t not in keep_tags:
                t.delete()

        # for t in tag_data:
        #     tag = Tag.objects.get(name=t['name'])
        #     instance.tags.add(tag)

        return instance
