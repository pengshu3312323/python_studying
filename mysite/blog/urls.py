'''blog's URLConfig'''

from django.urls import path,include
from django.views.generic import ListView,DetailView,DeleteView
from . import views
from .models import Blog_post

app_name = 'blog'

urlpatterns=[
        #Homepage of blog
        path('',views.index,name='index'),
        #posts of blog
        path(
            'post/',
            ListView.as_view(
                queryset=Blog_post.objects.order_by('-time_added'),
                context_object_name='posts',
                template_name='blog/post.html'
                ),
            name='post'
            ),
        #information of blog
        path(
            'about/',
            DetailView.as_view(
                model='Blog_post',
                context_object_name='post',
                template_name='blog/post_detail.html'
                ),
            name='about'
            ),
        #create a post
        path('post/create/',views.create_post,name='create_post'),
        #delete a post       
        path('post/<int:post_id>/delete/',views.post_delete,name='post_delete'),
        #Edit the information of the blog
        path('post/about/edit',views.blog_info_edit,name='blog_info_edit'),
        #One post of the blog
        path('post/<int:post_id>',views.post_detail,name='post_detail'),
        #Edit each blog post
        path('post/<int:post_id>/edit',views.post_edit,name='post_edit'),
        ]

