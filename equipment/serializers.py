from rest_framework import serializers

from .models import Brand, Camera, Film, Lens


class BrandNameSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='equipment:brand-detail-api'
    )

    class Meta:
        model = Brand
        fields = [
            'url',
            'name',
        ]


class CameraSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='equipment:camera-detail-api'
    )
    brand = BrandNameSerializer()

    class Meta:
        model = Camera
        fields = [
            'id',
            'url',
            'brand',
            'name',
        ]

    def create(self, validated_data):
        brand_data = validated_data.pop('brand')
        brand, created = Brand.objects.get_or_create(name=brand_data['name'])
        camera = Camera.objects.create(**validated_data, brand=brand)
        return camera


class FilmSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='equipment:film-detail-api'
    )
    brand = BrandNameSerializer()

    class Meta:
        model = Film
        fields = [
            'id',
            'url',
            'brand',
            'name'
        ]

    def create(self, validated_data):
        brand_data = validated_data.pop('brand')
        brand, created = Brand.objects.get_or_create(name=brand_data['name'])
        film = Film.objects.create(**validated_data, brand=brand)
        return film


class LensSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='equipment:lens-detail-api'
    )
    brand = BrandNameSerializer()

    class Meta:
        model = Lens
        fields = [
            'id',
            'url',
            'brand',
            'name'
        ]

    def create(self, validated_data):
        brand_data = validated_data.pop('brand')
        brand, created = Brand.objects.get_or_create(name=brand_data['name'])
        lens = Lens.objects.create(**validated_data, brand=brand)
        return lens


class BrandSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='equipment:brand-detail-api'
    )

    cameras = CameraSerializer(many=True)
    film = FilmSerializer(many=True)
    lenses = LensSerializer(many=True)

    class Meta:
        model = Brand
        fields = [
            'id',
            'url',
            'name',
            'cameras',
            'film',
            'lenses',
        ]

    def create(self, validated_data):
        cameras = validated_data.pop('cameras')
        film = validated_data.pop('film')
        lenses = validated_data.pop('lenses')

        brand = Brand.objects.create(**validated_data)

        for camera in cameras:
            Camera.objects.create(**camera, brand=brand)
        for film in film:
            Film.objects.create(**film, brand=brand)
        for lens in lenses:
            Lens.objects.create(**lens, brand=brand)

        return brand

    # TODO: Maybe add update method
