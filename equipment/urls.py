from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views.templates import CameraDetail, FilmDetail, LensDetail
from .views.viewsets import BrandViewSet, CameraViewSet, FilmViewSet, LensViewSet

app_name = 'equipment'

# Templates

urlpatterns = [
    path('camera/<int:pk>', CameraDetail.as_view(), name='camera_detail'),
    path('film/<int:pk>',   FilmDetail.as_view(),   name='film_detail'),
    path('lens/<int:pk>',   LensDetail.as_view(),   name='lens_detail'),
]

# API endpoints

api_url = 'api/equipment/'

list_actions = {'get': 'list', 'post': 'create'}
detail_actions = {'get': 'retrieve', 'delete': 'destroy'}

brand_list = BrandViewSet.as_view(list_actions)
camera_list = CameraViewSet.as_view(list_actions)
film_list = FilmViewSet.as_view(list_actions)
lens_list = LensViewSet.as_view(list_actions)

brand_detail = BrandViewSet.as_view(detail_actions)
camera_detail = CameraViewSet.as_view(detail_actions)
film_detail = FilmViewSet.as_view(detail_actions)
lens_detail = LensViewSet.as_view(detail_actions)

router = DefaultRouter()
router.register('brands', BrandViewSet)
router.register('cameras', CameraViewSet)
router.register('film', FilmViewSet)
router.register('lenses', LensViewSet)

urlpatterns += [
    path(api_url, include(router.urls)),
    path(api_url + 'brand/<int:pk>/',  brand_detail,  name='brand-detail-api'),
    path(api_url + 'camera/<int:pk>/', camera_detail, name='camera-detail-api'),
    path(api_url + 'film/<int:pk>/',   film_detail,   name='film-detail-api'),
    path(api_url + 'lens/<int:pk>/',   lens_detail,   name='lens-detail-api')
]
