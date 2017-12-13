'''Guide's URLconfig'''

from django.urls import path
from . import views

app_name = 'guide'

urlpatterns=[
        #Homepage of guide
        path('',views.index,name='index'),
        #Edit the favorite site
        path('edit/',views.edit,name='edit'),
        ]
