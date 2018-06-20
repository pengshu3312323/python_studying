'''Form model in the app Users'''
from django.contrib.auth.models import User
from django.db.models import Model
from django import forms 

class Register_form(forms.Form):
    '''User register form'''
    username=forms.CharField(label='Username',max_length=20)
    password1=forms.CharField(label='Password',widget=forms.PasswordInput)
    password2=forms.CharField(label='Password(Comfirm)',widget=forms.PasswordInput)

    def __str__(self):
        return self.__doc__

