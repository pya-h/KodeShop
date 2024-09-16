from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='honey_admin')),
    path('panel/', admin.site.urls, name='darbarian'),
    path('', views.home, name="home"),
    path('store/', include('store.urls')),
    path('stack/', include('stack.urls')),
    path('purchase/', include('purchase.urls')),
    path('user/', include('user.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('search/', views.search, name='search'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]