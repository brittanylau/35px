from django.contrib import admin
from .models import Post

# Register your models here.
# admin.site.register(Photographer)
class PostAdmin(admin.ModelAdmin):
    list_display = ('photographer', 'posted_on', 'title', 'caption')
    list_filter = ()
    search_fields = ['title', 'photographer']

admin.site.register(Post, PostAdmin)
