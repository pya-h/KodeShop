from django.contrib import admin
from .models import BlogPost, VideoPost


class BlogPostsAdminPanel(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'created_at')
    list_display_links = ('id', 'title', )


class VideoPostsAdminPanel(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'created_at')
    list_display_links = ('id', 'title', )


admin.site.register(BlogPost, BlogPostsAdminPanel)
admin.site.register(VideoPost, VideoPostsAdminPanel)