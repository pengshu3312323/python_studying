from django.db import models
from django.forms import ModelForm

class Favorite(models.Model):
    '''User's favorite web'''
    name=models.CharField(max_length=50)
    address=models.URLField()
    time_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

#------------------Model Forms-------------------

class Favorite_form(ModelForm):
    '''Form of adding favorite site'''
    class Meta:
        model=Favorite
        fields=['name','address']

