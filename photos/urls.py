from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (
    # Templates
    TagList, TagDetail,
    PostList, PostDetail, PostCreate, PostUpdate, PostDelete,
    CommentCreate, CommentUpdate, CommentDelete,

    # API endpoints
    TagViewSet, PostViewSet, CommentViewSet
)

app_name = 'photos'
api_url = 'api/posts/'

router = DefaultRouter()
router.register('tags', TagViewSet)
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)

tag_list = TagViewSet.as_view({'get': 'list'})
post_list = PostViewSet.as_view({'get': 'list'})
comment_list = CommentViewSet.as_view({'get': 'list'})

tag_detail = TagViewSet.as_view({
    'get': 'retrieve',
    'patch': 'update'
})
post_detail = PostViewSet.as_view({
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
    path('', PostList.as_view(), name='home'),

    path('tags', TagList.as_view(), name='tag_list'),
    path('tag/<int:pk>', TagDetail.as_view(), name='tag_detail'),

    path('post/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('post/create', PostCreate.as_view(), name='post_create'),
    path('post/<int:pk>/update', PostUpdate.as_view(), name='post_edit'),
    path('post/<int:pk>/delete', PostDelete.as_view(), name='post_delete'),

    path('post/<int:pk>/comment', CommentCreate.as_view(), name='comment_create'),
    path('post/<int:pk>/comment/update', CommentUpdate.as_view(), name='comment_edit'),
    path('post/<int:pk>/comment/delete', CommentDelete.as_view(), name='comment_delete'),

    # API endpoints
    path(api_url, include(router.urls)),
    path(api_url + 'tag/<int:pk>', tag_detail, name='tag-detail-api'),
    path(api_url + 'post/<int:pk>', post_detail, name='post-detail-api'),
    path(api_url + 'comment/<int:pk>', comment_detail, name='comment-detail-api'),
]
