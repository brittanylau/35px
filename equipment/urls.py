from django.urls import path
from . import views

app_name = 'equipment'

urlpatterns = [
    path('camera/<int:pk>', views.CameraDetail.as_view(), name='camera_detail'),
    path('film/<int:pk>',   views.FilmDetail.as_view(),   name='film_detail'),
    path('lens/<int:pk>',   views.LensDetail.as_view(),   name='lens_detail'),
]
