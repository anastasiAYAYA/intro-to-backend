from django.contrib import admin
from django.urls import path
from .views import get_index, get_todos, delete_todo, get_info, get_todo_list

urlpatterns = [
    path('', get_index, name='todos'),
    path('todos/', get_todos, name='todos'),
    path('todos/<int:pk>', get_info, name='todos_info'),
    path('todos/<int:pk>/delete', delete_todo, name='delete_todo'),
    path('todos/todo-list', get_todo_list, name='todo-list'),
    ]
