from django.urls import include, path
from rest_framework import routers

from . import views

app_name = 'users'

router = routers.DefaultRouter()
router.register('profiles', views.UserProfileViewSet)
router.register('', views.UserViewSet)

urlpatterns = [

    # Templates
    path('users',         views.UserList.as_view(),     name='user_list'),
    path('user/<int:pk>', views.UserDetail.as_view(),   name='user_detail'),
    path('signup/', views.SignUp.as_view(), name='signup'),

    # API endpoints
    path('api/users/', include(router.urls)),

]
