from rest_framework import serializers

from .models import Camera, Film, Lens


class CameraSerializer(serializers.HyperlinkedModelSerializer):
    brand = serializers.StringRelatedField()
    url = serializers.HyperlinkedIdentityField(
        view_name='equipment:camera-detail-api'
    )

    class Meta:
        model = Camera
        fields = ['id', 'url', 'brand', 'name']


class FilmSerializer(serializers.HyperlinkedModelSerializer):
    brand = serializers.StringRelatedField()
    url = serializers.HyperlinkedIdentityField(
        view_name='equipment:film-detail-api'
    )

    class Meta:
        model = Film
        fields = ['id', 'url', 'brand', 'name']


class LensSerializer(serializers.HyperlinkedModelSerializer):
    brand = serializers.StringRelatedField()
    url = serializers.HyperlinkedIdentityField(
        view_name='equipment:lens-detail-api'
    )

    class Meta:
        model = Lens
        fields = ['id', 'url', 'brand', 'name']
