from django.urls import path

from . import views

app_name = 'feed'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:photo_id>/', views.detail, name='detail'),
    path('<int:photo_id>/comment/', views.comment, name='comment'),
    path('post/', views.post, name='post'),
]
