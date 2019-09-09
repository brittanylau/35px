from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import UserProfile

AUTH_DIR = 'registration/'


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
    template_name = AUTH_DIR + 'signup.html'
