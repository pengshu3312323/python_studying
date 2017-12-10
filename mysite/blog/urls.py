'''blog's URLConfig'''

from django.urls import path,include
from . import views

app_name = 'blog'
urlpatterns=[
        #page of blog
        path('',views.index,name='index'),
        #posts of blog
        path('post/',views.post,name='post'),
        #information of blog
        path('about/',views.about,name='about'),
        #create a post
        path('post/create/',views.create_post,name='create_post'),
        #Edit the information of the blog
        path('post/about/edit',views.blog_info_edit,name='blog_info_edit'),
        ]

