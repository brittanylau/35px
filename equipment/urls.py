from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('cameras', views.CameraViewSet)
router.register('film', views.FilmViewSet)
router.register('lens', views.LensViewSet)

urlpatterns = [
    path('camera/<int:pk>', views.CameraDetail.as_view(), name='camera_detail'),
    path('film/<int:pk>', views.FilmDetail.as_view(), name='film_detail'),
    path('lens/<int:pk>', views.LensDetail.as_view(), name='lens_detail'),

    path('api/equipment/', include(router.urls)),
]
