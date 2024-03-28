from django.contrib import admin
from django.urls import path
from .views import login_page, register_page, logout

urlpatterns = [
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('logout/', logout, name='logout')
    # path('forgot-password/',),
    # path('reset-password/'),
]
