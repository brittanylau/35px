from django.views.generic import DetailView

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Brand, Camera, Film, Lens
from .serializers import (
    BrandSerializer,
    CameraSerializer,
    FilmSerializer,
    LensSerializer,
)


# Templates


class CameraDetail(DetailView):
    model = Camera


class FilmDetail(DetailView):
    model = Film


class LensDetail(DetailView):
    model = Lens


# API endpoints


class BrandViewSet(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CameraViewSet(ModelViewSet):
    queryset = Camera.objects.all()
    serializer_class = CameraSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class FilmViewSet(ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class LensViewSet(ModelViewSet):
    queryset = Lens.objects.all()
    serializer_class = LensSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
