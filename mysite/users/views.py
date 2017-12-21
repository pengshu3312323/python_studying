from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout,login,authenticate

def user_login(request):
    '''User login'''
    username=request.POST('username')
    password=request.POST('password')
    user=authenticate(request,username=username,password=password)
    if user is not None:
        login(request,user)
        return redirect('guide:index')

def register(request):
    '''User register'''
    return render('users/register.html')

def user_logout(request):
    '''User log out'''
    logout(request)
    return HttpResponseRedirect(reverse('guide:index'))




