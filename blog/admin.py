from django.contrib import admin
from .models import BlogPost


class BlogsAdminPanel(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'created_at')
    list_display_links = ('id', 'title', )


admin.site.register(BlogPost, BlogsAdminPanel)