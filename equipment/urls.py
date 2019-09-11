from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CameraDetail, FilmDetail, LensDetail  # Templates
from .views import BrandViewSet, CameraViewSet, FilmViewSet, LensViewSet  # API views

app_name = 'equipment'
api_url = 'api/equipment/'

router = DefaultRouter()
router.register('brands', BrandViewSet)
router.register('cameras', CameraViewSet)
router.register('film', FilmViewSet)
router.register('lenses', LensViewSet)

brand_list = BrandViewSet.as_view({
    'get': 'list',
    'post': 'create',
    'patch': 'update',
})
brand_detail = BrandViewSet.as_view({
    'get': 'retrieve',
    'patch': 'update',
    'delete': 'destroy',
})
camera_list = CameraViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
camera_detail = CameraViewSet.as_view({
    'get': 'retrieve',
    'delete': 'destroy',
})
film_list = FilmViewSet.as_view({'get': 'list'})
film_detail = FilmViewSet.as_view({'get': 'retrieve'})
lens_list = LensViewSet.as_view({'get': 'list'})
lens_detail = LensViewSet.as_view({'get': 'retrieve'})

urlpatterns = [
    # Templates
    path('camera/<int:pk>', CameraDetail.as_view(), name='camera_detail'),
    path('film/<int:pk>',   FilmDetail.as_view(),   name='film_detail'),
    path('lens/<int:pk>',   LensDetail.as_view(),   name='lens_detail'),

    # API endpoints
    path(api_url, include(router.urls)),
    path(api_url + 'brand/<int:pk>/', brand_detail, name='brand-detail-api'),
    path(api_url + 'camera/<int:pk>/', camera_detail, name='camera-detail-api'),
    path(api_url + 'film/<int:pk>/', film_detail, name='film-detail-api'),
    path(api_url + 'lens/<int:pk>/', lens_detail, name='lens-detail-api')
]
