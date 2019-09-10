from django.views.generic import DetailView
from rest_framework import viewsets

from .models import Camera, Film, Lens
from .serializers import CameraSerializer, FilmSerializer, LensSerializer


# Templates


class CameraDetail(DetailView):
    model = Camera
    template_name = 'camera_detail.html'


class FilmDetail(DetailView):
    model = Film
    template_name = 'film_detail.html'


class LensDetail(DetailView):
    model = Lens
    template_name = 'lens_detail.html'


# API endpoints


class CameraViewSet(viewsets.ModelViewSet):
    queryset = Camera.objects.all()  # .order_by('brand')
    serializer_class = CameraSerializer


class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()  # .order_by('brand')
    serializer_class = FilmSerializer


class LensViewSet(viewsets.ModelViewSet):
    queryset = Lens.objects.all()  # .order_by('brand')
    serializer_class = LensSerializer
