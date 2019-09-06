from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import User, Tag, Post, Comment

USER_TEMPLATE_DIR="feed/users/"
TAG_TEMPLATE_DIR="feed/tags/"
POST_TEMPLATE_DIR="feed/posts/"
COMMENT_TEMPLATE_DIR="feed/comments/"

# USERS


class UserList(ListView):
    model = User
    ordering = ['name']
    template_name=USER_TEMPLATE_DIR + "user_list.html"

class UserDetail(DetailView):
    model = User
    template_name=USER_TEMPLATE_DIR + "user_detail.html"

# TAGS

class TagList(ListView):
    model = Tag
    ordering = ['name'] # popularity of tag
    template_name=TAG_TEMPLATE_DIR + "tag_list.html"

class TagDetail(DetailView):
    model = Tag
    template_name=TAG_TEMPLATE_DIR + "tag_detail.html"

# POSTS

class PostList(ListView):
    model = Post
    ordering = ['-posted_on']
    template_name=POST_TEMPLATE_DIR + "post_list.html"

class PostDetail(DetailView):
    model = Post
    template_name=POST_TEMPLATE_DIR + "post_detail.html"

class PostCreate(CreateView):
    model = Post
    fields = [ 'user', 'image', 'title', 'caption', 'taken_on', 'tags' ]
    template_name=POST_TEMPLATE_DIR + "post_form.html"

class PostUpdate(UpdateView):
    model = Post
    fields = [ 'title', 'caption', 'taken_on', 'tags' ]
    template_name=POST_TEMPLATE_DIR + "post_form.html"

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('feed:post_list')
    template_name=POST_TEMPLATE_DIR + "post_confirm_delete.html"

# COMMENTS

class CommentList(ListView):
    model = Comment
    ordering = ['posted_on']
    template_name=COMMENT_TEMPLATE_DIR + 'comment_list.html'

class CommentCreate(CreateView):
    model = Comment
    fields = [ 'user', 'post', 'text' ]
    template_name=COMMENT_TEMPLATE_DIR + "comment_form.html"

class CommentUpdate(UpdateView):
    model = Comment
    fields = [ 'user', 'text' ]
    template_name=COMMENT_TEMPLATE_DIR + "comment_form.html"

class CommentDelete(DeleteView):
    model = Comment
    template_name=COMMENT_TEMPLATE_DIR + "comment_confirm_delete.html"

    def get_success_url(self):
        return reverse_lazy('feed:post_detail', kwargs={'pk': self.object.post.id})
