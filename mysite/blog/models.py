from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

def upload_to(instance,filename):
    '''file will be uploaded to MEDIA_ROOT/<username>/<filename>'''
    return ''.format(instance.owner.username,filename)

class Blog_post(models.Model):
    '''Post of blog'''
    title=models.CharField(max_length=100)
    body=models.TextField()
    time_added=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to=upload_to,blank=True)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        '''return doc of class'''
        return self.title

class Information(models.Model):
    '''info of the blog'''
    blog_name=models.CharField(max_length=50)
    blog_writer=models.CharField(max_length=30)
    blog_describe=models.TextField()
    owner=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        '''return the name of class'''
        return self.blog_name

############ModelForms#####################

class Post_form(ModelForm):
    class Meta:
        model=Blog_post
        fields=['title','body']

class Blog_info_form(ModelForm):
    class Meta:
        model=Information
        fields=['blog_name','blog_describe']

