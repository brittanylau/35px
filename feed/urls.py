from django.urls import path, include
from . import views

app_name = 'feed'

urlpatterns = [

    path('', views.PostList.as_view(), name='home'),

    # USERS
    path('users',         views.UserList.as_view(),     name='user_list'),
    path('user/<int:pk>', views.UserDetail.as_view(),   name='user_detail'),
    path('signup/', views.SignUp.as_view(), name='signup'),

    # TAGS
    path('tags',          views.TagList.as_view(),      name='tag_list'),
    path('tag/<int:pk>',  views.TagDetail.as_view(),    name='tag_detail'),

    # GEAR
    path('camera/<int:pk>', views.CameraDetail.as_view(), name='camera_detail'),
    path('film/<int:pk>',   views.FilmDetail.as_view(),   name='film_detail'),
    path('lens/<int:pk>',   views.LensDetail.as_view(),   name='lens_detail'),

    # POSTS
    path('post/<int:pk>',        views.PostDetail.as_view(),   name='post_detail'),
    path('post/create',          views.PostCreate.as_view(),   name='post_create'),
    path('post/<int:pk>/update', views.PostUpdate.as_view(),   name='post_edit'),
    path('post/<int:pk>/delete', views.PostDelete.as_view(),   name='post_delete'),

    # COMMENTS
    path('post/<int:pk>/comments/',      views.CommentList.as_view(),   name='comment_list'),
    path('post/<int:pk>/comment/create', views.CommentCreate.as_view(), name='comment_create'),
    path('post/<int:pk>/comment/update', views.CommentUpdate.as_view(), name='comment_edit'),
    path('post/<int:pk>/comment/delete', views.CommentDelete.as_view(), name='comment_delete'),

]
