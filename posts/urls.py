from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('tags', views.TagViewSet)
router.register('posts', views.PostViewSet)
router.register('comments', views.CommentViewSet)

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
    path('api/posts/', include(router.urls)),
]
