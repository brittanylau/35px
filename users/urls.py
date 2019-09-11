from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserList, UserDetail, SignUp  # Templates
from .views import UserViewSet, ProfileViewSet   # API views

app_name = 'users'
api_url = 'api/users/'

list_actions = {'get': 'list'}
detail_actions = {'get': 'retrieve'}

user_list = UserViewSet.as_view(list_actions)
profile_list = ProfileViewSet.as_view(list_actions)

user_detail = UserViewSet.as_view(detail_actions)
profile_detail = ProfileViewSet.as_view(detail_actions)

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('profiles', ProfileViewSet)

urlpatterns = [
    # Templates
    path('users',         UserList.as_view(),   name='user_list'),
    path('user/<int:pk>', UserDetail.as_view(), name='user_detail'),
    path('signup/',       SignUp.as_view(),     name='signup'),

    # API endpoints
    path(api_url, include(router.urls)),
    path(
        api_url + 'user/<int:pk>/',
        user_detail,
        name='user-detail-api'
    ),
    path(
        api_url + 'profile/<int:pk>/',
        profile_detail,
        name='profile-detail-api'
    ),
]
