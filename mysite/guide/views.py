from django.shortcuts import render
from .models import Favorite

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
