from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import User, UserProfile
from .serializers import UserSerializer, UserProfileSerializer


# Templates


class UserList(ListView):
    model = UserProfile


class UserDetail(DetailView):
    model = UserProfile


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


# API endpoints


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'tags': reverse(
            'users:user-list-api',
            request=request, format=format
        ),
        'posts': reverse(
            'users:profile-list-api',
            request=request, format=format
        )
    })


class UserListAPI(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserProfileListAPI(ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserProfileDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
