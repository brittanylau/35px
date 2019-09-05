from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post, Comment

# POSTS

class PostList(ListView):
    model = Post
    ordering = ['-posted_on']
    paginate_by = 20

class PostDetail(DetailView):
    model = Post

class PostCreate(CreateView):
    model = Post
    fields = [ 'title', 'caption', 'taken_on' ]

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
    fields = [ 'commenter', 'text' ]

class CommentUpdate(UpdateView):
    model = Comment
    fields = [ 'text' ]

class CommentDelete(DeleteView):
    model = Comment
    success_url = reverse_lazy('feed:post_list') # maybe send back to post detail later
