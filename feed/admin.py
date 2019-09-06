from django.contrib import admin
from .models import User, Location, Tag, Brand, Camera, Film, Post, Comment

class LocationAdmin(admin.ModelAdmin):
    list_display = ('city', 'country')

class CameraAdmin(admin.ModelAdmin):
    list_display = ('brand', 'name')

class FilmAdmin(admin.ModelAdmin):
    list_display = ('brand', 'name')

class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'posted_on', 'title', 'caption')
    list_filter = ()
    search_fields = ['title', 'user']

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'text', 'posted_on')

admin.site.register(User)
admin.site.register(Camera, CameraAdmin)
admin.site.register(Film, FilmAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag)
admin.site.register(Brand)
admin.site.register(Location, LocationAdmin)
