##########################################
#----View functions for the 'guide' page----- 
#
#----Written by Peng Shu
##########################################

from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Favorite
from .search import baidu

def index(request):
    '''Homepage of guide'''

    if request.method=='POST':
        keywords=request.POST['keywords']
        url=baidu(keywords)
        return redirect(url)

    if request.user.is_authenticated:
        favorite=Favorite.objects.filter(owner=request.user).order_by('time_added')
    
    else:
        favorite=None

    context={'favorite':favorite,}
    return render(request,'guide/index.html',context)

def edit(request):
    '''Edit my favorite site'''
    if request.user.is_authenticated:
        if request.method!='POST':
            favorites=Favorite.objects.order_by('time_added')
            context={'favorites':favorites,}
            return render(request,'guide/edit.html',context)
        elif request.method=='POST':
            ids=request.POST.getlist('favorite')#Which you want to delete
            for i in ids:
                site=Favorite.objects.get(pk=i)
                site.delete()
            return HttpResponseRedirect(reverse('guide:edit'))
    else:
        return render(request,'users/login_or_register.html')

protocol=('http','ftp')

@login_required
def add(request):
    '''Add a new fovorite site'''
    if request.method=='POST':
        name=request.POST['name']
        address=request.POST['address']
        if not address.startswith(protocol): 
            #Check whether the user add the protocol or not
            address = 'http://'+address

        new_site=Favorite.objects.create(name=name,address=address,owner=request.user)
        new_site.save()
        return HttpResponseRedirect(reverse('guide:edit'))

    return render(request,'guide/add.html')

