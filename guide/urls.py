#####################################################
# ----URLconfig of 'guide' page---
#
# ----Written by:Peng Shu---
####################################################

from django.urls import path

from . import views

app_name = 'guide'

urlpatterns = [
        # Homepage of guide
        path('', views.index, name='index'),
        # Edit the favorite site
        path('edit/', views.edit, name='edit'),
        # Add a new favorite site
        path('edit/add/', views.add, name='add'),
        ]
