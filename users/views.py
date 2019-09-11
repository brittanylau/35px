from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from rest_framework.viewsets import ReadOnlyModelViewSet

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


class UserViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileViewSet(ReadOnlyModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
