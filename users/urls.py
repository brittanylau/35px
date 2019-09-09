from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [

    # USERS
    path('users',         views.UserList.as_view(),     name='user_list'),
    path('user/<int:pk>', views.UserDetail.as_view(),   name='user_detail'),
    path('signup/', views.SignUp.as_view(), name='signup'),

]
