from django.shortcuts import render
from .models import Favorite,Favorite_form
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    '''Homepage of guide'''
    favorite=Favorite.objects.all()
    context={'favorite':favorite}
    return render(request,'guide/index.html',context)

def edit(request):
    '''Edit my favorite site'''
    favorites=Favorite.objects.order_by('time_added')
    context={'favorites':favorites}
    return render(request,'guide/edit.html',context)

def add(request):
    '''Add a new fovorite site'''
    if request.method!='POST':
        form=Favorite_form()
    elif request.method=='POST':
        form=Favorite_form(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('guide:edit'))

    context={'form':form}
    return render(request,'guide/add.html',context)
