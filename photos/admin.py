from django.contrib import admin
from .models import Tag, Photo, Comment


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('author', 'posted_on', 'image', 'title', 'caption')
    list_filter = ()
    search_fields = ['title', 'author']


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'photo', 'text', 'posted_on')


admin.site.register(Photo, PhotoAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag)
