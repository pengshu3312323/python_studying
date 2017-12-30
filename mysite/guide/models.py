from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

class Favorite(models.Model):
    '''User's favorite web'''
    name=models.CharField(max_length=50)
    address=models.TextField()
    time_added=models.DateTimeField(auto_now_add=True)
    owner=models.ForeignKey(User,on_delete=models.CASCADE,)

    def __str__(self):
        return self.name

#------------------Model Forms-------------------

class Favorite_form(ModelForm):
    '''Form of adding favorite site'''
    class Meta:
        model=Favorite
        fields=['name','address']

