from django.urls import path
from . import views

app_name = 'feed'

urlpatterns = [
    path('',                views.PostList.as_view(),   name='post_list'),
    path('post/<int:pk>',   views.PostDetail.as_view(), name='post_detail'),
    path('create',          views.PostCreate.as_view(), name='post_create'),
    path('update/<int:pk>', views.PostUpdate.as_view(), name='post_edit'),
    path('delete/<int:pk>', views.PostDelete.as_view(), name='post_delete'),

    path('post/<int:pk>/comments/', views.CommentList.as_view(), name='comment_list'),
    path('post/<int:pk>/comment/create', views.CommentCreate.as_view(), name='comment_create'),
    path('post/<int:pk>/comment/update', views.CommentUpdate.as_view(), name='comment_edit'),
    path('post/<int:pk>/comment/delete/', views.CommentDelete.as_view(), name='comment_delete'),
]
