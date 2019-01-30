##########################################
# ----View functions for the 'guide' page-----
#
# ----Written by Peng Shu
##########################################

import random

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.cache import cache

from users.handler import SiteUserSessionCtr
from guide.models import Favorite
from util.response import Response
from util.cache import CustomCache


def index(request):
    '''Homepage of guide'''

    context = {
        'favorite': None,
        'username': None,
    }

    if not SiteUserSessionCtr.login_check(request):
        return render(request, 'guide/index.html', context)

    user_id = request.session['user_id']
    username = request.session['username']

    cache_key = 'favorites_{}'.format(user_id)
    favorite_data = cache.get(cache_key)

    if not favorite_data:
        favorites = Favorite.objects.filter(owner__id=user_id).order_by('time_added')
        favorite_data = [f.get_data() for f in favorites]
        context = {'favorite': favorite_data}
        CustomCache.set(cache_key, favorite_data, 60 * 60 * 10)

    context['username'] = username
    context['favorite'] = favorite_data

    if request.GET.get('json'):
        return Response.data(data=context)
    return render(request, 'guide/index.html', context)


def edit(request):
    '''Edit my favorite site'''
    if request.user.is_authenticated:
        if request.method != 'POST':
            favorites = Favorite.objects.filter(owner=request.user).order_by('time_added')
            context = {
                'favorites': favorites,
                }

            return render(request, 'guide/edit.html', context)
        elif request.method == 'POST':
            user_id = request.user.id
            cache_key = 'favorites_{}'.format(user_id)
            ids = request.POST.getlist('favorite')  # Which you want to delete
            for i in ids:
                site = Favorite.objects.get(pk=i)
                site.delete()
                # 更新缓存
                # TODO 复用
                favorites = Favorite.objects.filter(owner__id=user_id).order_by('time_added')
                favorite_data = [f.get_data() for f in favorites]
                context = {'favorite': favorite_data}
                CustomCache.set(cache_key, context, 60 * 60 * 10)

            return HttpResponseRedirect(reverse('guide:edit'))
    else:
        return render(request, 'users/login_or_register.html')


@login_required
def add(request):
    '''Add a new fovorite site'''
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        user_id = request.user.id

        if not address.startswith(('http', 'ftp')):
            # Check whether the user add the protocol or not
            address = 'http://' + address

        new_site = Favorite.objects.create(name=name, address=address, owner=request.user)
        new_site.save()
        # 更新缓存
        # TODO 复用
        cache_key = 'favorites_{}'.format(user_id)
        favorites = Favorite.objects.filter(owner__id=user_id).order_by('time_added')
        favorite_data = [f.get_data() for f in favorites]
        context = {'favorite': favorite_data}
        CustomCache.set(cache_key, context, 60 * 60 * 10)

        return HttpResponseRedirect(reverse('guide:edit'))

    return render(request, 'guide/add.html')
