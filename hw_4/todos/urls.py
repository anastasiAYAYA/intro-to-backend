from django.contrib import admin
from django.urls import path
from .views import (get_index, get_info, delete_todo, edit_todo, edit_category, get_category_info,
                    delete_category, index)

urlpatterns = [
    path('', index, name='todo-lists'),
    path('todo-lists/', get_index, name='todo-lists'),
    path('todos/<int:pk>', get_info, name='todos_info'),
    path('todos/<int:pk>/delete', delete_todo, name='todo_delete'),
    path('todos/<int:pk>/edit', edit_todo, name='todo_edit'),
    path('todo-lists/<int:pk>', get_category_info, name='category_info'),
    path('todo-lists/<int:pk>/delete', delete_category, name='category_delete'),
    path('todo-lists/<int:pk>/edit', edit_category, name='category_edit'),
]