from django.contrib import admin
from .models import BlogPost


class BlogsAdminPanel(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'created_at')


admin.site.register(BlogPost, BlogsAdminPanel)