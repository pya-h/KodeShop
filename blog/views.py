# views.py
from django.shortcuts import render
from .models import BlogPost
from django.shortcuts import render, redirect, get_object_or_404


def show_post(request, post_id: int):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'blogs/post.html', {'post': post})
