from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from .forms import Register_form


# Not in using
def user_login(request):
    '''User login'''
    if request.method != 'POST':
        form = AuthenticationForm()
    elif request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('guide:index'))

    context ={'form': form, }
    return render(request, 'users/login.html', context)


def register(request):
    '''User register'''
    if request.method != 'POST':
        form = Register_form()
    elif request.method == 'POST':
        form = Register_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']

            # Check the whether the username is existed or not
            if len(User.objects.filter(username=username)) == 0:
                # Check the 2 input password are same
                if password1 and password2 and (password1 == password2):
                    user = User.objects.create_user(username=username, password=password1)
                    user.save()
                    login(request, user)
                    return HttpResponseRedirect(reverse('guide:index'))
                else:
                    form = Register_form()
                    context = {'form': form, 'error1': 'dismatch'}
                    return render(request, 'users/register.html', context)
            else:
                form = Register_form()
                context = {'form': form, 'error2': 'existed'}
                return render(request, 'users/register.html', context)

    context = {'form': form}
    return render(request, 'users/register.html', context)


# Not in using
def user_logout(request):
    '''User log out'''
    logout(request)
    return HttpResponseRedirect(reverse('guide:index'))
