from django.urls import path
from . import views

urlpatterns = [
    path('blogs/<int:blog_id>/', views.show_blog, name="blog_post"),
    path('blogs/', views.list_blog_posts, name="blogs"),
    path('videos/<int:video_post_id>/', views.list_video_posts, name="video_post"),
    path('videos/', views.list_video_posts, name="videos"),
]
