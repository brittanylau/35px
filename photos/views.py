from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Tag, Photo, Comment
from .serializers import TagSerializer, PhotoSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly


# Templates

TAG_TEMPLATE_DIR = 'tags/'
PHOTO_TEMPLATE_DIR = 'photos/'
COMMENT_TEMPLATE_DIR = 'comments/'


class TagList(ListView):
    model = Tag
    ordering = ['name']
    template_name = TAG_TEMPLATE_DIR + 'tag_list.html'


class TagDetail(DetailView):
    model = Tag
    template_name = TAG_TEMPLATE_DIR + 'tag_detail.html'


class PhotoList(ListView):
    model = Photo
    ordering = ['-posted_on']
    template_name = PHOTO_TEMPLATE_DIR + 'photo_list.html'


class PhotoDetail(DetailView):
    model = Photo
    template_name = PHOTO_TEMPLATE_DIR + 'photo_detail.html'


class PhotoCreate(CreateView):
    model = Photo
    fields = [
        'author',
        'image',
        'title',
        'caption',
        # 'taken_on',
        'camera',
        'film',
        'lens',
        'exposure',
        'aperture',
        'shutter_speed',
        'tags'
    ]
    template_name = PHOTO_TEMPLATE_DIR + 'photo_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super(PhotoCreate, self).form_valid(form)


class PhotoUpdate(UpdateView):
    model = Photo
    fields = [
        'title',
        'caption',
        # 'taken_on',
        'camera',
        'film',
        'lens',
        'exposure',
        'aperture',
        'shutter_speed',
        'tags'
    ]
    template_name = PHOTO_TEMPLATE_DIR + 'photo_edit.html'


class PhotoDelete(DeleteView):
    model = Photo
    success_url = reverse_lazy('photos:home')
    template_name = PHOTO_TEMPLATE_DIR + 'photo_confirm_delete.html'


class CommentList(ListView):
    model = Comment
    ordering = ['-posted_on']
    template_name = COMMENT_TEMPLATE_DIR + 'comment_list.html'


class CommentCreate(CreateView):
    model = Comment
    fields = ['photo', 'text']
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
            'photos:photo_detail',
            kwargs={'pk': self.object.photo.id}
        )


# API endpoints


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all().order_by('name')
    serializer_class = TagSerializer


class PhotoViewSet(ModelViewSet):
    queryset = Photo.objects.all().order_by('-posted_on')
    serializer_class = PhotoSerializer

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

    def get_permissions(self):
        permission_classes = [IsAuthenticatedOrReadOnly]
        if self.action != 'list':
            permission_classes += [IsAuthorOrReadOnly]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.profile)
