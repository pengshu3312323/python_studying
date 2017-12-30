from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.models import User 
from .forms import Register_form 

#Not in using
def user_login(request):
    '''User login'''
    username=request.POST('username')
    password=request.POST('password')
    user=authenticate(request,username=username,password=password)
    if user is not None:
        login(request,user)
        return HttpResponseRedirect(reverse('blog:post'))
#    else
        

def register(request):
    '''User register'''
    
    if request.method!='POST':
        form=Register_form()
    elif request.method=='POST':
        form=Register_form(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password1=form.cleaned_data['password1']
            password2=form.cleaned_data['password2']
            
            #Check the whether the username is exist or not
            if User.objects.filter(username=username) is not None:
                #Check the 2 input password are same
                if password1 and password2 and (password1==password2):
                    user=User.objects.create_user(username=username,password=password1)
                    user.save()
                    login(request,user)
                    return HttpResponseRedirect(reverse('guide:index'))
                else:
                    error='Error:2 passwords are different'
                    context={error:'error'}
                    return render(request,'users/register_fail.html',context)
            else:
                error='Error:Username is exist'
                context={error:'error'}
                return render(request,'users/register_fail.html',context)

    context={'form':form}
    return render(request,'users/register.html',context)


#Not in using
def user_logout(request):
    '''User log out'''
    logout(request)
    return HttpResponseRedirect(reverse('guide:index'))




