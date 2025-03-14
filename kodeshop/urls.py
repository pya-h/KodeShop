from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from django.views.static import serve
from django.conf import settings
from messaging.views import contact_us
from category.sitemaps import CategorySitemap
from post.sitemaps import BlogPostSitemap, VideoPostSitemap
from store.sitemaps import ProductSitemap
from django.contrib.sitemaps.views import sitemap as sitemap_views

sitemaps  = {
    'categories': CategorySitemap,
    'blogs': BlogPostSitemap,
    'videoposts': VideoPostSitemap,
    'products': ProductSitemap
}

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='honey_admin')),
    path('panel/', admin.site.urls, name='admin-panel'),
    path('', views.home, name="home"),
    path('store/', include('store.urls')),
    path('stack/', include('stack.urls')),
    path('purchase/', include('purchase.urls')),
    path('user/', include('user.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('search/', views.search, name='search'),
    path('about/', views.about_us, name='about'),
    path('contact/', contact_us, name='contact'),
    path('messaging/', include('messaging.urls')),
    path('posts/', include('post.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
    path('ckeditor5/upload-video/', views.upload_video, name='upload_video'),
    path('sitemap.xml', sitemap_views, {"sitemaps": sitemaps}, name='sitemap'),
    path('robots.txt', include('robots.urls')),
]
