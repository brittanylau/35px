from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Tag, Post, Comment
from .serializers import TagSerializer, PostSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly


# Templates

TAG_TEMPLATE_DIR = 'tags/'
POST_TEMPLATE_DIR = 'posts/'
COMMENT_TEMPLATE_DIR = 'comments/'


class TagList(ListView):
    model = Tag
    ordering = ['name']
    template_name = TAG_TEMPLATE_DIR + 'tag_list.html'


class TagDetail(DetailView):
    model = Tag
    template_name = TAG_TEMPLATE_DIR + 'tag_detail.html'


class PostList(ListView):
    model = Post
    ordering = ['-posted_on']
    template_name = POST_TEMPLATE_DIR + 'post_list.html'


class PostDetail(DetailView):
    model = Post
    template_name = POST_TEMPLATE_DIR + 'post_detail.html'


class PostCreate(CreateView):
    model = Post
    fields = [
        'author', 'image', 'title', 'caption', 'taken_on',
        'camera', 'film', 'lens',
        'exposure', 'aperture', 'shutter_speed',
        'tags'
    ]
    template_name = POST_TEMPLATE_DIR + 'post_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super(CommentCreate, self).form_valid(form)


class PostUpdate(UpdateView):
    model = Post
    fields = [
        'title', 'caption', 'taken_on',
        'camera', 'film', 'lens',
        'exposure', 'aperture', 'shutter_speed',
        'tags'
    ]
    template_name = POST_TEMPLATE_DIR + 'post_edit.html'


class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('posts:home')
    template_name = POST_TEMPLATE_DIR + 'post_confirm_delete.html'


class CommentList(ListView):
    model = Comment
    ordering = ['-posted_on']
    template_name = COMMENT_TEMPLATE_DIR + 'comment_list.html'


class CommentCreate(CreateView):
    model = Comment
    fields = ['post', 'text']
    template_name = COMMENT_TEMPLATE_DIR + 'comment_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super(CommentCreate, self).form_valid(form)


class CommentUpdate(UpdateView):
    model = Comment
    fields = ['author', 'text']
    template_name = COMMENT_TEMPLATE_DIR + 'comment_edit.html'


class CommentDelete(DeleteView):
    model = Comment
    template_name = COMMENT_TEMPLATE_DIR + 'comment_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy(
            'posts:post_detail',
            kwargs={'pk': self.object.post.id}
        )


# API endpoints


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all().order_by('name')
    serializer_class = TagSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all().order_by('-posted_on')
    serializer_class = PostSerializer

    def get_permissions(self):
        permission_classes = [IsAuthenticatedOrReadOnly]
        if self.action != 'list':
            permission_classes += [IsAuthorOrReadOnly]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.profile)


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all().order_by('-posted_on')
    serializer_class = CommentSerializer
    """
    def get_permissions(self):
        permission_classes = [IsAuthenticatedOrReadOnly]
        if self.action != 'list':
            permission_classes += [IsAuthorOrReadOnly]
        return [permission() for permission in permission_classes]
    """

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.profile)
