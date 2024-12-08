# views.py
from django.shortcuts import render
from .models import BlogPost, VideoPost
from django.shortcuts import render, get_object_or_404
from kodeshop.utils import PaginationParams

def show_blog(request, blog_id: int):
    blog = get_object_or_404(BlogPost, id=blog_id)
    return render(request, 'posts/blog.html', {'blog': blog})

def show_video(request, video_post_id: int):
    video = get_object_or_404(VideoPost, id=video_post_id)
    return render(request, 'posts/video.html', {'video': video})


def list_blog_posts(request):
    pagination = PaginationParams(request, BlogPost)
    blogs = pagination.get_items('created_at', order_descending=True)
    return render(request, 'posts/index.html', {'posts': blogs, 'pagination': pagination, })

def list_video_posts(request):
    pagination = PaginationParams(request, VideoPost)
    videos = pagination.get_items('created_at', order_descending=True)
    return render(request, 'posts/index.html', {'posts': videos, 'pagination': pagination, })