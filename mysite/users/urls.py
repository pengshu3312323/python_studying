'''URLconfig for users'''

from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.models import User
from . import views

app_name='users'

urlpatterns = [
        #login page
        path(
            'login/',
            LoginView.as_view(
                template_name='users/login.html',
#                redirect_field_name='blog:index',
                ),
            name='login'),
        #Log our page
        path('logout/',
            LogoutView.as_view(
                next_page='guide:index',
                ),
            name='logout'),
        #register page
        path('register/',views.register,name='register'),
        ]

