from django.contrib import admin
from .models import Tag, Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'posted_on', 'title', 'caption')
    list_filter = ()
    search_fields = ['title', 'author']


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'text', 'posted_on')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag)
