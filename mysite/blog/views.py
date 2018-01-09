from django.shortcuts import render,get_object_or_404,get_list_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import Permission
from django.contrib.auth.decorators import login_required,permission_required

from .models import Blog_post,Information,Post_image
from .forms import Post_form,Information_form

def index(request):
    '''Homepage of the blog'''
    return render(request,'blog/index.html')

def post(request):
    '''Post page of blog'''
    posts=Blog_post.objects.order_by('-time_added')
    images=Post_image.objects.all()
    perm_flag=request.user.has_perm('blog.add_Blog_post') #check permission
    context={'posts':posts,'perm_flag':perm_flag,'images':images}
    return render(request,'blog/post.html',context)

def about(request):
    '''information of blog'''
    info=Information.objects.all().filter(pk=1)
    perm_flag=request.user.has_perm('blog.chenge_Information')#check permission
    context={'info':info,'perm_flag':perm_flag}
    return render(request,'blog/about.html',context)

@login_required
@permission_required('blog.add_Blog_post')
def create_post(request):
    '''create a new post'''
    if request.method!='POST':
        form=Post_form()
    elif request.method=='POST':
        form=Post_form(request.POST,request.FILES)
        if form.is_valid():
            title=form.cleaned_data['title']
            body=form.cleaned_data['body']
            image=form.cleaned_data['image']

            new_post=Blog_post.objects.create(title=title,body=body)
            new_post.save()
            new_image=Post_image(
                    post=new_post,
                    image=request.FILES['image']
                    )    
            new_image.save()
            return HttpResponseRedirect(reverse('blog:post'))

    context={'form':form}
    return render(request,'blog/createpost.html',context)

@login_required
@permission_required('blog.change_Information')
def blog_info_edit(request):
    '''Edit the information of the blog'''
    info=Information.objects.get(pk=1)
    if request.method!='POST':
        form=Blog_info_form(instance=info)
    elif request.method=='POST':
        form=Blog_info_form(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('blog:about'))

    context={'form':form}
    return render(request,'blog/blog_info_edit.html',context)

def post_detail(request,post_id):
    '''Single post'''
    post=get_object_or_404(Blog_post,pk=post_id)
    images=Post_image.objects.filter(post=post_id)
    #check the permission
    perm_flag=request.user.has_perm('blog.change_Blog_post') \
            and request.user.has_perm('blog.Delete_Blog_post')
    context={'post':post,'perm_flag':perm_flag,'images':images}
    return render(request,'blog/post_detail.html',context)

@login_required
@permission_required('blog.change_Blog_post')
def post_edit(request,post_id):
    '''Edit each post'''
    if request.method!='POST':
        #bound the post to the form
        post=Blog_post.objects.get(pk=post_id)
        data={
            'title':post.title,
            'body':post.body,
                }
        form=Post_form(data)
    elif request.method=='POST':
        form=Post_form(request.POST,request.FILES)
        if form.is_valid():
            title=form.cleaned_data['title']
            body=form.cleaned_data['body']
            image=request.FILES['image']
            #update the post
            post=Blog_post.objects.get(pk=post_id)
            post.title=title
            post.body=body
            #update the post image
            image=Post_image.objects.create(image=image,post=post)
            post.post_image_set.set([image,])
            post.save()
        return HttpResponseRedirect(reverse('blog:post'))

    context={'form':form}
    return render(request,'blog/post_edit.html',context)

@login_required
@permission_required('blog.delete_Blog_post')
def post_delete(request,post_id):
    '''Delete a post'''
    post=get_object_or_404(Blog_post,pk=post_id)
    post.delete()
    return HttpResponseRedirect(reverse('blog:post'))
