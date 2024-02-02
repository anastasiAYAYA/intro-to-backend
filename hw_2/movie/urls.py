from django.contrib import admin
from django.urls import path
from .views import get_index, get_info

urlpatterns = [
    path('movies', get_index),
    path('movies/<int:pk>', get_info)
]