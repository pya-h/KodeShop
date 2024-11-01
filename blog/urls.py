from django.urls import path
from . import views

urlpatterns = [
    path('<int:post_id>/', views.show_post, name="blog_post"),
    path('', views.list_blogs, name="blogs"),
]
