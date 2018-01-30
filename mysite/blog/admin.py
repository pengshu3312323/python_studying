###################################################
#---Admin Config for 'blog' app---
#
#---Written by:Peng Shu
###################################################

from django.contrib import admin

from blog.models import Blog_post,Information,Post_image,Background

class Blog_post_admin(admin.ModelAdmin):
    list_display=('title','time_added')

class Post_image_admin(admin.ModelAdmin):
        list_display=('image',)

class Blog_info_admin(admin.ModelAdmin):
    list_display=('blog_name','blog_writer','blog_describe')

class Background_admin(admin.ModelAdmin):
    list_display=('image',)

admin.site.register(Blog_post,Blog_post_admin)
admin.site.register(Information,Blog_info_admin)
admin.site.register(Post_image,Post_image_admin)
admin.site.register(Background,Background_admin)
