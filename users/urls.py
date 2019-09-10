from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'users'
api_url = 'api/users/'

urlpatterns = format_suffix_patterns([
    # Templates
    path('users',         views.UserList.as_view(),   name='user_list'),
    path('user/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('signup/',       views.SignUp.as_view(),     name='signup'),

    # API endpoints
    path(api_url, views.api_root),
    path(
        api_url + 'users',
        views.UserListAPI.as_view(),
        name='user-list-api'
    ),
    path(
        api_url + 'user/<int:pk>/',
        views.UserDetailAPI.as_view(),
        name='user-detail-api'
    ),
    path(
        api_url + 'profiles/',
        views.UserProfileListAPI.as_view(),
        name='profile-list-api'
    ),
    path(
        api_url + 'profile/<int:pk>/',
        views.UserProfileDetailAPI.as_view(),
        name='profile-detail-api'
    ),
])
