from django.shortcuts import render,get_object_or_404,get_list_or_404
from blog.models import Blog_post,Post_image,Information,Post_form,Blog_info_form
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def index(request):
    '''Homepage of the blog'''
    return render(request,'blog/index.html')
'''
def post(request):
    Post of blog
    posts=Blog_post.objects.order_by('-time_added')
    context={'posts':posts}
    return render(request,'blog/post.html',context)
'''
def about(request):
    '''information of blog'''
    info=Information.objects.get()
    context={'info':info}
    return render(request,'blog/about.html',context)

@login_required
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

@login_required
def blog_info_edit(request):
    '''Edit the information of the blog'''
    info=Information.objects.get()
    if request.method!='POST':
        form=Blog_info_form(instance=info)
    elif request.method=='POST':
        form=Blog_info_form(instance=info,data=request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('blog:about'))

    context={'form':form}
    return render(request,'blog/blog_info_edit.html',context)

def post_detail(request,post_id):
    '''Single post'''
    post=get_object_or_404(Blog_post,pk=post_id)
    images=Post_image.objects.all().filter(post_id=post_id).order_by('id')
    context={'post':post,'images':images}
    return render(request,'blog/post_detail.html',context)

@login_required 
def post_edit(request,post_id):
    '''Edit each post'''
    post=get_object_or_404(Blog_post,pk=post_id)
    if request.method!='POST':
        form=Post_form(instance=post)
    elif request.method=='POST':
        form=Post_form(instance=post,data=request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('blog:post'))

    context={
        'post':post,
        'form':form,
        }
    return render(request,'blog/post_edit.html',context)

@login_required 
def post_delete(request,post_id):
    '''Delete a post'''
    post=get_object_or_404(Blog_post,pk=post_id)
    post.delete()
    return HttpResponseRedirect(reverse('blog:post'))
