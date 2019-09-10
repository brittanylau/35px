from rest_framework import serializers

from .models import Camera, Film, Lens


class CameraSerializer(serializers.HyperlinkedModelSerializer):
    brand = serializers.ReadOnlyField(source='brand.name')

    class Meta:
        model = Camera
        fields = ['id', 'brand', 'name']


class FilmSerializer(serializers.HyperlinkedModelSerializer):
    brand = serializers.ReadOnlyField(source='brand.name')

    class Meta:
        model = Film
        fields = ['id', 'brand', 'name']


class LensSerializer(serializers.HyperlinkedModelSerializer):
    brand = serializers.ReadOnlyField(source='brand.name')

    class Meta:
        model = Lens
        fields = ['id', 'brand', 'name']
