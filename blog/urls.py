#######################################################
#---URLConfig of 'blog' page---
#
#---Written by:Peng Shu
#######################################################

from django.urls import path,include
from django.views.generic import ListView,DetailView,DeleteView

from . import views
from .models import Blog_post

app_name = 'blog'

urlpatterns=[
        #Homepage of blog
        path('',views.index,name='index'),
        #posts of blog
        path('post/',views.post,name='post'),
        #information of blog
        path('about/',views.about,name='about'),
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

