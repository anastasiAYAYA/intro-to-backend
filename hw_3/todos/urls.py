from django.contrib import admin
from django.urls import path
from .views import get_index, get_list, get_info, delete_todo

urlpatterns = [
    path('', get_index, name='index'),
    path('todos/index', get_index, name='index'),
    path('todos/', get_list, name='todos'),
    path('todos/todos', get_list, name='todos'),
    path('todos/<int:pk>', get_info, name='todos_info'),
    path('todos/todos/<int:pk>', get_info, name='todos_info'),
    path('todos/<int:pk>/delete', delete_todo, name='todo_delete'),
    path('todos/todos/<int:pk>/delete', delete_todo, name='todo_delete')
]
