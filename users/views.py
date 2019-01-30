from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from .models.data import HINT
from .forms import Register_form
from .handler import SiteUserHandler, SiteUserSessionCtr


def user_login(request):
    '''User login'''
    if request.method != 'POST':
        return render(request, 'users/login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        res = SiteUserHandler.login(
            login_type=0,
            username=username,
            password=password
        )

        if res[0]:
            # 登陆成功
            user_data = res[-1]
            user_id = user_data['id']
            username = user_data['username']

            SiteUserSessionCtr.login(request, user_id, username)
            return redirect(reverse('guide:index'))
        else:
            error_no = res[-1]
            error = HINT[error_no][-1]
            context = {'username': username, 'error': error}
            return render(request, 'users/login.html', context)


def register(request):
    '''User register'''
    if request.method != 'POST':
        return render(request, 'users/register.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        error = None

        if password != password_confirm:
            # 两次密码不相同,提示编号为4
            error = HINT[4][-1]
            context = {'username': username, 'error': error}
            return render(request, 'users/register.html', context)
        else:
            res = SiteUserHandler.register(
                0, username=username, password=password
            )

            if res[0]:
                user_data = res[-1]
                user_id = user_data['id']
                username = user_data['username']

                SiteUserSessionCtr.login(request, user_id, username)
                return redirect(reverse('guide:index'))
            else:
                error_no = res[-1]
                error = HINT[error_no][-1]
        context = {'username': username, 'error': error}
        return render(request, 'users/register.html', context)


def user_logout(request):
    '''User log out'''
    res = SiteUserSessionCtr.logout(request)
    print(res)
    return redirect(reverse('guide:index'))
