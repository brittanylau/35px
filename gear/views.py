from django.views.generic import DetailView
from .models import Camera, Film, Lens


class CameraDetail(DetailView):
    model = Camera
    template_name = 'camera_detail.html'


class FilmDetail(DetailView):
    model = Film
    template_name = 'film_detail.html'


class LensDetail(DetailView):
    model = Lens
    template_name = 'lens_detail.html'
