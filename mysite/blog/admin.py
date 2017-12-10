from django.contrib import admin
from blog.models import Blog_post,Information

class Blog_post_admin(admin.ModelAdmin):
    list_display=('title','time_added')

class Blog_info_admin(admin.ModelAdmin):
    list_display=('blog_name','blog_writer','blog_describe')

admin.site.register(Blog_post,Blog_post_admin)
admin.site.register(Information,Blog_info_admin)

