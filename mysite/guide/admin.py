from django.contrib import admin
from .models import Favorite

class Favorite_admin(admin.ModelAdmin):
    '''Favorite site in admin page'''
    list_display=('name','address',)

admin.site.register(Favorite,Favorite_admin)
