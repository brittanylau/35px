from django.contrib import admin
from .models import Brand, Camera, Film, Lens


class CameraAdmin(admin.ModelAdmin):
    list_display = ('brand', 'name')


class FilmAdmin(admin.ModelAdmin):
    list_display = ('brand', 'name')


class LensAdmin(admin.ModelAdmin):
    list_display = ('brand', 'name')


admin.site.register(Brand)
admin.site.register(Camera, CameraAdmin)
admin.site.register(Film, FilmAdmin)
admin.site.register(Lens, LensAdmin)
