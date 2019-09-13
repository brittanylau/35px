from django.views.generic import DetailView
from ..models import Camera, Film, Lens


class CameraDetail(DetailView):
    model = Camera


class FilmDetail(DetailView):
    model = Film


class LensDetail(DetailView):
    model = Lens
