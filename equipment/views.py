from django.views.generic import DetailView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

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


class CameraListAPI(ListCreateAPIView):
    queryset = Camera.objects.all()
    serializer_class = CameraSerializer


class CameraDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Camera.objects.all()
    serializer_class = CameraSerializer


class FilmListAPI(ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


class FilmDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


class LensListAPI(ListCreateAPIView):
    queryset = Lens.objects.all()
    serializer_class = LensSerializer


class LensDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Lens.objects.all()
    serializer_class = LensSerializer
