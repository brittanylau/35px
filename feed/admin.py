from django.contrib import admin
from .models import User, Tag, Post, Comment

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')

class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'posted_on', 'title', 'caption')
    list_filter = ()
    search_fields = ['title', 'user']

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'text', 'posted_on')

admin.site.register(User, UserAdmin)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
