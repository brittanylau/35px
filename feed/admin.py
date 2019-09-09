from django.contrib import admin
from .models import UserProfile, Tag, Brand, Camera, Film, Lens, Post, Comment

class CameraAdmin(admin.ModelAdmin):
    list_display = ('brand', 'name')

class FilmAdmin(admin.ModelAdmin):
    list_display = ('brand', 'name')

class LensAdmin(admin.ModelAdmin):
    list_display = ('brand', 'name')

class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'posted_on', 'title', 'caption')
    list_filter = ()
    search_fields = ['title', 'author']

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'text', 'posted_on')

admin.site.register(UserProfile)
admin.site.register(Camera, CameraAdmin)
admin.site.register(Film, FilmAdmin)
admin.site.register(Lens, LensAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag)
admin.site.register(Brand)
