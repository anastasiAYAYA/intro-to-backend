from django.contrib import admin
from django.urls import path
from .views import get_index, get_info, get_main

urlpatterns = [
    path('', get_main),
    path('articles', get_index),
    path('articles/<int:pk>', get_info)
]