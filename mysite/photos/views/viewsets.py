from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from ..models import Tag, Photo, Comment
from ..serializers import (
    TagSerializer, PhotoSerializer, CommentSerializer, PhotoFileSerializer
)
from ..permissions import IsAuthorOrReadOnly


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all().order_by('name')
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


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


class ImageUploadView(APIView):
    parser_class = (FileUploadParser,)
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request, *args, **kwargs):
        file_serializer = PhotoFileSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save(author=self.request.user.profile)
            return Response(
                file_serializer.data,
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                file_serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
