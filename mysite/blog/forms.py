'''Forms in blog'''

from django import forms
from django.db import models

from .models import Information

class Post_form(forms.Form):
    '''The form for blog post creation or edit'''
    title=forms.CharField(label='Post title',max_length=100)
    body=forms.CharField(label='Post body',widget=forms.Textarea)
    image=forms.ImageField(label='Image',required=False)

class Information_form(forms.ModelForm):
    '''Form for blog information edit'''
    class Meta:
        model=Information
        fields=['blog_name','blog_writer','blog_describe',]
