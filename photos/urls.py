from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (
    # Templates
    TagList, TagDetail,
    PhotoList, PhotoDetail, PhotoCreate, PhotoUpdate, PhotoDelete,
    CommentCreate, CommentUpdate, CommentDelete,

    # API endpoints
    TagViewSet, PhotoViewSet, CommentViewSet
)

app_name = 'photos'
api_url = 'api/photos/'

router = DefaultRouter()
router.register('tags', TagViewSet)
router.register('photos', PhotoViewSet)
router.register('comments', CommentViewSet)

tag_list = TagViewSet.as_view({'get': 'list'})
post_list = PhotoViewSet.as_view({'get': 'list'})
comment_list = CommentViewSet.as_view({'get': 'list'})

tag_detail = TagViewSet.as_view({
    'get': 'retrieve',
    'patch': 'update'
})
post_detail = PhotoViewSet.as_view({
    'get': 'retrieve',
    'patch': 'update',
    'delete': 'destroy'
})
comment_detail = CommentViewSet.as_view({
    'get': 'retrieve',
    'patch': 'update',
    'delete': 'destroy'
})

urlpatterns = [
    # Templates
    path('', PhotoList.as_view(), name='home'),

    path('tags', TagList.as_view(), name='tag_list'),
    path('tag/<int:pk>', TagDetail.as_view(), name='tag_detail'),

    path('photo/<int:pk>', PhotoDetail.as_view(), name='post_detail'),
    path('photo/create', PhotoCreate.as_view(), name='post_create'),
    path('photo/<int:pk>/update', PhotoUpdate.as_view(), name='post_edit'),
    path('photo/<int:pk>/delete', PhotoDelete.as_view(), name='post_delete'),

    path('photo/<int:pk>/comment', CommentCreate.as_view(), name='comment_create'),
    path('photo/<int:pk>/comment/update', CommentUpdate.as_view(), name='comment_edit'),
    path('photo/<int:pk>/comment/delete', CommentDelete.as_view(), name='comment_delete'),

    # API endpoints
    path(api_url, include(router.urls)),
    path(api_url + 'tag/<int:pk>', tag_detail, name='tag-detail-api'),
    path(api_url + 'photo/<int:pk>', post_detail, name='post-detail-api'),
    path(api_url + 'comment/<int:pk>', comment_detail, name='comment-detail-api'),
]
