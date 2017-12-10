from django.shortcuts import render
from blog.models import Blog_post,Information,Post_form,Blog_info_form
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

def index(request):
    '''Homepage of MeetPencil'''
    return render(request,'blog/index.html')

def post(request):
    '''Post of blog'''
    posts=Blog_post.objects.order_by('-time_added')
    context={'posts':posts}
    return render(request,'blog/post.html',context)

def about(request):
    '''information of blog'''
    info=Information.objects.get()
    context={'info':info}
    return render(request,'blog/about.html',context)

def create_post(request):
    '''create a new post'''
    if request.method!='POST':
        form=Post_form()
    elif request.method=='POST':
        form=Post_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog:post'))

    context={'form':form}
    return render(request,'blog/createpost.html',context)

def blog_info_edit(request):
    '''Edit the information of the blog'''
    if request.method!='POST':
        form=Blog_info_form()
    elif request.method=='POST':
        form=Blog_info_form(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('blog:about'))

    context={'form':form}
    return render(request,'blog/blog_info_edit.html',context)

