from django.views.generic import DetailView

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets

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


class CameraViewSet(viewsets.ModelViewSet):
    queryset = Camera.objects.all()
    serializer_class = CameraSerializer


class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


class LensViewSet(viewsets.ModelViewSet):
    queryset = Lens.objects.all()
    serializer_class = LensSerializer
