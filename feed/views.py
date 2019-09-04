# from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse, Http404
# from django.template import loader
# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post

# Create your views here.
class PostList(ListView):
    model = Post

class PostDetail(DetailView):
    model = Post

class PostCreate(CreateView):
    model = Post
    fields = [ 'title', 'caption', 'posted_on', 'taken_on' ]

class PostUpdate(UpdateView):
    model = Post
    fields = [ 'title', 'caption' ]

class PostDelete(DeleteView):
    model = Post
