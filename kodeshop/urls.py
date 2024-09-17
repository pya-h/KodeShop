from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from django.views.static import serve
from django.conf import settings
from messaging.views import contact_us

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
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
