from django.shortcuts import render
from .models import Favorite,Favorite_form
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def index(request):
    '''Homepage of guide'''
    if request.user.is_authenticated:
        favorite=Favorite.objects.all().filter(owner=request.user).order_by('time_added')
    
    else:
        favorite=None

    context={'favorite':favorite}
    return render(request,'guide/index.html',context)

def edit(request):
    '''Edit my favorite site'''
    if request.user.is_authenticated:
        favorites=Favorite.objects.order_by('time_added')
        context={'favorites':favorites}
        return render(request,'guide/edit.html',context)
    else:
        return render(request,'users/login_or_register.html')

@login_required
def add(request):
    '''Add a new fovorite site'''
    if request.method!='POST':
        form=Favorite_form()
    elif request.method=='POST':
        form=Favorite_form(request.POST)
        if form.is_valid():
            new_site=form.save(commit=False)
            new_site.owner=request.user
            new_site.save()
        return HttpResponseRedirect(reverse('guide:edit'))

    context={'form':form}
    return render(request,'guide/add.html',context)
