from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from ..models import UserProfile


class UserList(ListView):
    model = UserProfile


class UserDetail(DetailView):
    model = UserProfile


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
