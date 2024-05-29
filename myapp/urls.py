from django.urls import path
from . import views

urlpatterns = [
    path('isalive/', views.is_alive, name='is_alive'),
    path('timestamp/', views.timestamp, name='timestamp'),
]