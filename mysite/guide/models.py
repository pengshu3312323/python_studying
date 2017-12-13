from django.db import models
from django import forms

class Favorite(models.Model):
    '''User's favorite web'''
    name=models.CharField(max_length=50)
    address=models.URLField(max_length=100)
    time_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

#------------------Model Forms-------------------

class Favorite_form(forms.ModelForm):
    '''Form of adding favorite site'''
    name=forms.CharField(label='Name',max_length=50)
    address=forms.URLField(label='Address',max_length=100)

