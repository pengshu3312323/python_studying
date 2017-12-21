'''URLconfig for users'''

from django.urls import path
from django.contrib.auth.views import login
from django.contrib.auth.models import User
from . import views

app_name='users'

urlpatterns = [
        #login page
        path('login/',login,{'template_name':'users/login.html'},name='login'),
        #Log our page
        path('logout/',views.user_logout,name='logout'),
        #register page
        path('register/',views.register,name='register'),
        ]

