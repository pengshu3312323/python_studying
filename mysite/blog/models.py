from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

def upload_to(instance,filename):
    '''file will be uploaded to MEDIA_ROOT/<post_title>/<filename>'''
    return '{0}/{1}'.format(instance.post.title,filename)

class Blog_post(models.Model):
    '''Post of blog'''
    title=models.CharField(max_length=100)
    body=models.TextField()
    time_added=models.DateTimeField(auto_now_add=True)
#    owner=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        '''return doc of class'''
        return self.title

class Post_image(models.Model):
    '''Images in post'''
    image=models.ImageField(upload_to=upload_to)
    post=models.ForeignKey(Blog_post,on_delete=models.CASCADE,verbose_name='the image in the post')

    def __str__(self):
        return self.__doc__

class Information(models.Model):
    '''info of the blog'''
    blog_name=models.CharField(max_length=50)
    blog_writer=models.CharField(max_length=30)
    blog_describe=models.TextField()

    def __str__(self):
        '''return the name of class'''
        return self.blog_name

