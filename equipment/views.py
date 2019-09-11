from django.views.generic import DetailView

from rest_framework.viewsets import ModelViewSet

from .models import Camera, Film, Lens
from .serializers import CameraSerializer, FilmSerializer, LensSerializer


# Templates


class CameraDetail(DetailView):
    model = Camera


class FilmDetail(DetailView):
    model = Film


class LensDetail(DetailView):
    model = Lens


# API endpoints


class CameraViewSet(ModelViewSet):
    queryset = Camera.objects.all()
    serializer_class = CameraSerializer


class FilmViewSet(ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


class LensViewSet(ModelViewSet):
    queryset = Lens.objects.all()
    serializer_class = LensSerializer
