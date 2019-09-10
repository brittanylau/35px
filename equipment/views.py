from django.views.generic import DetailView

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

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


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'cameras': reverse(
            'equipment:camera-list-api',
            request=request, format=format
        ),
        'film': reverse(
            'equipment:film-list-api',
            request=request, format=format
        ),
        'lenses': reverse(
            'equipment:lens-list-api',
            request=request, format=format
        )
    })


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
