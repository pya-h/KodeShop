from django.urls import path
from . import views

urlpatterns = [
    path('blogs/<id:uint>', views.send_support_message, name="send_support_message"),
]
