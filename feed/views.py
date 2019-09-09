from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import UserProfile, Tag, Camera, Film, Lens, Post, Comment

TEMPLATE_DIR='feed/'
AUTH_DIR='registration/'
USER_TEMPLATE_DIR = TEMPLATE_DIR + 'users/'
TAG_TEMPLATE_DIR = TEMPLATE_DIR + 'tags/'
GEAR_TEMPLATE_DIR = TEMPLATE_DIR + 'gear/'
CAMERA_TEMPLATE_DIR = GEAR_TEMPLATE_DIR + 'cameras/'
FILM_TEMPLATE_DIR = GEAR_TEMPLATE_DIR + 'film/'
LENS_TEMPLATE_DIR = GEAR_TEMPLATE_DIR + 'lenses/'
POST_TEMPLATE_DIR = TEMPLATE_DIR + 'posts/'
COMMENT_TEMPLATE_DIR = TEMPLATE_DIR + 'comments/'

# USERS

class UserList(ListView):
    model = UserProfile
    # ordering = ['username']
    template_name = USER_TEMPLATE_DIR + 'user_list.html'

class UserDetail(DetailView):
    model = UserProfile
    template_name = USER_TEMPLATE_DIR + 'user_detail.html'

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = AUTH_DIR + 'signup.html'

# TAGS

class TagList(ListView):
    model = Tag
    ordering = ['name'] # popularity of tag
    template_name = TAG_TEMPLATE_DIR + 'tag_list.html'

class TagDetail(DetailView):
    model = Tag
    template_name = TAG_TEMPLATE_DIR + 'tag_detail.html'

# GEAR

class CameraDetail(DetailView):
    model = Camera
    template_name = CAMERA_TEMPLATE_DIR + 'camera_detail.html'

class FilmDetail(DetailView):
    model = Film
    template_name = FILM_TEMPLATE_DIR + 'film_detail.html'

class LensDetail(DetailView):
    model = Lens
    template_name = LENS_TEMPLATE_DIR + 'lens_detail.html'

# POSTS

class PostList(ListView):
    model = Post
    ordering = ['-posted_on']
    template_name = POST_TEMPLATE_DIR + 'post_list.html'

class PostDetail(DetailView):
    model = Post
    template_name = POST_TEMPLATE_DIR + 'post_detail.html'

class PostCreate(CreateView):
    model = Post
    fields = [ 'image', 'title', 'caption', 'taken_on', 'camera', 'film', 'lens', 'exposure', 'aperture', 'shutter_speed', 'tags' ]
    template_name = POST_TEMPLATE_DIR + 'post_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super(CommentCreate, self).form_valid(form)

class PostUpdate(UpdateView):
    model = Post
    fields = [ 'title', 'caption', 'taken_on', 'camera', 'film', 'lens', 'exposure', 'aperture', 'shutter_speed', 'tags' ]
    template_name = POST_TEMPLATE_DIR + 'post_edit.html'

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('feed:post_list')
    template_name = POST_TEMPLATE_DIR + 'post_confirm_delete.html'

# COMMENTS

class CommentList(ListView):
    model = Comment
    ordering = ['-posted_on']
    template_name = COMMENT_TEMPLATE_DIR + 'comment_list.html'

class CommentCreate(CreateView):
    model = Comment
    fields = [ 'post', 'text' ]
    template_name = COMMENT_TEMPLATE_DIR + 'comment_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super(CommentCreate, self).form_valid(form)

class CommentUpdate(UpdateView):
    model = Comment
    fields = [ 'author', 'text' ]
    template_name = COMMENT_TEMPLATE_DIR + 'comment_edit.html'

class CommentDelete(DeleteView):
    model = Comment
    template_name = COMMENT_TEMPLATE_DIR + 'comment_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('feed:post_detail', kwargs={'pk': self.object.post.id})
