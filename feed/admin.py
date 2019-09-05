from django.contrib import admin
from .models import Post, Comment

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('photographer', 'posted_on', 'title', 'caption')
    list_filter = ()
    search_fields = ['title', 'photographer']

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'commenter', 'text', 'posted_on')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
