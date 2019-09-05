from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import User, Tag, Post, Comment

# USERS

class UserList(ListView):
    model = User
    ordering = ['name']

class UserDetail(DetailView):
    model = User

# TAGS

class TagList(ListView):
    model = Tag
    ordering = [] # popularity of tag

# POSTS

class PostList(ListView):
    model = Post
    ordering = ['-posted_on']

class PostDetail(DetailView):
    model = Post

class PostCreate(CreateView):
    model = Post
    fields = [ 'user', 'image', 'title', 'caption', 'taken_on' ]

class PostUpdate(UpdateView):
    model = Post
    fields = [ 'title', 'caption', 'taken_on' ]

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('feed:post_list')

# COMMENTS

class CommentList(ListView):
    model = Comment
    ordering = ['posted_on']

class CommentCreate(CreateView):
    model = Comment
    fields = [ 'user', 'post', 'text' ]

class CommentUpdate(UpdateView):
    model = Comment
    fields = [ 'user', 'text' ]

class CommentDelete(DeleteView):
    model = Comment

    def get_success_url(self):
        return reverse_lazy('feed:post_detail', kwargs={'pk': self.object.post.id})
