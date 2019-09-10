from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'equipment'
api_url = 'api/equipment/'

urlpatterns = format_suffix_patterns([
    # Templates
    path('camera/<int:pk>', views.CameraDetail.as_view(), name='camera_detail'),
    path('film/<int:pk>',   views.FilmDetail.as_view(),   name='film_detail'),
    path('lens/<int:pk>',   views.LensDetail.as_view(),   name='lens_detail'),

    # API endpoints
    path(api_url, views.api_root),
    path(
        api_url + 'cameras/',
        views.CameraListAPI.as_view(),
        name='camera-list-api'
    ),
    path(
        api_url + 'camera/<int:pk>/',
        views.CameraDetailAPI.as_view(),
        name='camera-detail-api'
    ),
    path(
        api_url + 'film/',
        views.FilmListAPI.as_view(),
        name='film-list-api'
    ),
    path(
        api_url + 'film/<int:pk>/',
        views.FilmDetailAPI.as_view(),
        name='film-detail-api'
    ),
    path(
        api_url + 'lenses/',
        views.LensListAPI.as_view(),
        name='lens-list-api'
    ),
    path(
        api_url + 'lens/<int:pk>/',
        views.LensDetailAPI.as_view(),
        name='lens-detail-api'
    )
])
