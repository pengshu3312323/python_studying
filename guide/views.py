##########################################
# ----View functions for the 'guide' page-----
#
# ----Written by Peng Shu
##########################################

import random

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from users.handler import SiteUserSessionCtr
from guide.handler import UserFavoriteHandler
from util.response import Response


def index(request):
    '''Homepage of guide'''

    context = {
        'favorite': None,
        'username': None,
    }

    login = SiteUserSessionCtr.login_check(request)
    if not login:
        return render(request, 'guide/index.html', context)

    user_id = login['id']
    username = login['username']
    handler = UserFavoriteHandler(user_id)

    favorite_data = handler.get_favorites()
    context = {
        'favorite': favorite_data,
        'username': username,
    }

    if request.GET.get('json'):
        return Response.data(data=context)
    return render(request, 'guide/index.html', context)


def edit(request):
    '''Edit my favorite site'''
    login = SiteUserSessionCtr.login_check(request)
    if not login:
        return render(request, 'users/login_or_register.html')
    else:
        user_id = login['id']
        username = login['username']
        handler = UserFavoriteHandler(user_id)

        if request.method != 'POST':
            favorite_data = handler.get_favorites()

            context = {
                'favorites': favorite_data,
                'username': username,
            }
            if request.GET.get('json'):
                return Response.data(data=context)
            return render(request, 'guide/edit.html', context)
        elif request.method == 'POST':

            ids = request.POST.getlist('favorite')  # Which you want to delete
            res = handler.delete_favorites(ids=ids)
            print(res)
            return HttpResponseRedirect(reverse('guide:edit'))


def add(request):
    '''Add a new fovorite site'''
    login = SiteUserSessionCtr.login_check(request)
    if not login:
        return render(request, 'users/login_or_register.html')
    else:
        if request.method == 'POST':
            user_id = login['id']
            handler = UserFavoriteHandler(user_id)
            name = request.POST['name']
            address = request.POST['address']
            handler.create_favorite(name, address)

            return HttpResponseRedirect(reverse('guide:edit'))
        return render(request, 'guide/add.html')
