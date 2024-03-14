from django.contrib import admin
from django.urls import path
from .views import index, get_todos, get_info

urlpatterns = [
    path('', index, name='todos'),
    path('todos/', get_todos, name='todos'),
    path('todos/<int:pk>', get_info, name='todos_info')
]