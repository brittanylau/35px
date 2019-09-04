from django.urls import path

from . import views

app_name = 'feed'
home = '/feed/posts/' # fix this later
urlpatterns = [
    path('posts/',          views.PostList.as_view(),   name='post_list'),
    path('post/<int:pk>',   views.PostDetail.as_view(), name='post_detail'),
    path('create',          views.PostCreate.as_view(success_url=home), name='post_create'),
    path('update/<int:pk>', views.PostUpdate.as_view(success_url=home), name='post_edit'),
    path('delete/<int:pk>', views.PostDelete.as_view(success_url=home), name='post_delete'),
]
