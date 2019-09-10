from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from rest_framework import viewsets

from .models import User, UserProfile
from .serializers import UserSerializer, UserProfileSerializer


# Templates


class UserList(ListView):
    model = UserProfile
    # ordering = ['username']
    template_name = 'user_list.html'


class UserDetail(DetailView):
    model = UserProfile
    template_name = 'user_detail.html'


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


# API endpoints

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()  # .order_by('username')
    serializer_class = UserProfileSerializer
