from django.urls import path
from . import views

urlpatterns = [
    path('support', views.send_support_message, name="send_support_message"),
]
