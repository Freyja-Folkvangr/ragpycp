from django.contrib import admin

# Register your models here.
from content.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'content']
    ordering = ['-added']

admin.site.register(Post, PostAdmin)