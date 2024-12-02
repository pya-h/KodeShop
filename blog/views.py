# views.py
from django.shortcuts import render
from .models import BlogPost
from django.shortcuts import render, get_object_or_404
from kodeshop.utils import PaginationParams

def show_post(request, post_id: int):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'blogs/post.html', {'post': post})


def list_blogs(request):
    pagination = PaginationParams(request, BlogPost)
    blogs = pagination.get_items('created_at', order_descending=True)
    return render(request, 'blogs/index.html', {'blogs': blogs})