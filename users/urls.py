'''URLconfig for users'''

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User

from . import views

app_name = 'users'

urlpatterns = [
        path('login/', views.user_login, name='login'),
        path('logout/', views.user_logout, name='logout'),
        path('register/', views.register, name='register'),
        ]
