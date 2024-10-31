# views.py
from django.shortcuts import render
from .models import BlogPost


def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'post.html', {'post': post})
