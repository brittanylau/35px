from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'posts'
api_url = 'api/posts/'

urlpatterns = [
    # Templates
    path('', views.PostList.as_view(), name='home'),

    path('tags',          views.TagList.as_view(),      name='tag_list'),
    path('tag/<int:pk>',  views.TagDetail.as_view(),    name='tag_detail'),

    path('post/<int:pk>',        views.PostDetail.as_view(),   name='post_detail'),
    path('post/create',          views.PostCreate.as_view(),   name='post_create'),
    path('post/<int:pk>/update', views.PostUpdate.as_view(),   name='post_edit'),
    path('post/<int:pk>/delete', views.PostDelete.as_view(),   name='post_delete'),

    path('post/<int:pk>/comments/',      views.CommentList.as_view(),   name='comment_list'),
    path('post/<int:pk>/comment/create', views.CommentCreate.as_view(), name='comment_create'),
    path('post/<int:pk>/comment/update', views.CommentUpdate.as_view(), name='comment_edit'),
    path('post/<int:pk>/comment/delete', views.CommentDelete.as_view(), name='comment_delete'),

    # API endpoints
    path(api_url, views.posts_api_root),
    path(
        api_url + 'tags/',
        views.TagListAPI.as_view(),
        name='tag_list_api'
    ),
    path(
        api_url + 'tag/<int:pk>',
        views.TagDetailAPI.as_view()
    ),
    path(
        api_url + 'posts/',
        views.PostListAPI.as_view(),
        name='post_list_api'
    ),
    path(
        api_url + 'post/<int:pk>',
        views.PostDetailAPI.as_view(),
    ),
    path(
        api_url + 'comments/',
        views.CommentListAPI.as_view(),
        name='comment_list_api'
    ),
    path(
        api_url + 'comment/<int:pk>',
        views.CommentDetailAPI.as_view()
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
