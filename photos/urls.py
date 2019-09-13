from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views.templates import (
    TagList, TagDetail,
    PhotoList, PhotoDetail, PhotoCreate, PhotoUpdate, PhotoDelete,
    CommentCreate, CommentUpdate, CommentDelete
)
from .views.viewsets import (
    TagViewSet, PhotoViewSet, CommentViewSet, ImageUploadView
)

app_name = 'photos'

# Templates

urlpatterns = [
    path('', PhotoList.as_view(), name='home'),

    path('tags', TagList.as_view(), name='tag_list'),
    path('tag/<int:pk>', TagDetail.as_view(), name='tag_detail'),

    path('photo/<int:pk>', PhotoDetail.as_view(), name='photo_detail'),
    path('photo/create', PhotoCreate.as_view(), name='photo_create'),
    path('photo/<int:pk>/update', PhotoUpdate.as_view(), name='photo_edit'),
    path('photo/<int:pk>/delete', PhotoDelete.as_view(), name='photo_delete'),

    path('photo/<int:pk>/comment', CommentCreate.as_view(), name='comment_create'),
    path('photo/<int:pk>/comment/update', CommentUpdate.as_view(), name='comment_edit'),
    path('photo/<int:pk>/comment/delete', CommentDelete.as_view(), name='comment_delete'),
]

# API endpoints

api_url = 'api/photos/'

list_actions = {'get': 'list', 'post': 'create'}
detail_actions = {'get': 'retrieve', 'patch': 'update', 'delete': 'destroy'}

tag_list = TagViewSet.as_view(list_actions)
photo_list = PhotoViewSet.as_view(list_actions)
comment_list = CommentViewSet.as_view(list_actions)

tag_detail = TagViewSet.as_view(detail_actions)
photo_detail = PhotoViewSet.as_view(detail_actions)
comment_detail = CommentViewSet.as_view(detail_actions)

router = DefaultRouter()
router.register('tags', TagViewSet)
router.register('photos', PhotoViewSet)
router.register('comments', CommentViewSet)

urlpatterns += [
    path(api_url, include(router.urls)),
    path(api_url + 'tags/<int:pk>', tag_detail, name='tag-detail-api'),
    path(api_url + 'photos/<int:pk>', photo_detail, name='photo-detail-api'),
    path(api_url + 'comments/<int:pk>', comment_detail, name='comment-detail-api'),
    path(api_url + 'upload', ImageUploadView.as_view(), name='image-upload-api')
]
