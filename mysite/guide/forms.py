'''Forms in guide'''

from django import forms

from .models import Favorite

class Search_form(forms.Form):
    '''The form to search on Internet'''
    keywords=forms.CharField(label='Search',max_length=50)
#    engine

