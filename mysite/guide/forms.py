#############################################
#---Forms in 'guide' app---
#
#---Writtrn by:Peng Shu---
#############################################
from django import forms

class Search_form(forms.Form):
    '''The form to search on Internet'''
    keywords=forms.CharField(label='Search',max_length=50)
#    engine

