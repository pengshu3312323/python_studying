#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# Models in the 'guide' app---
# Written by:Peng Shu

from django.db import models
from django.forms import model_to_dict

from users.models import SiteUser
from .base import TimeBaseModel


class Favorite(TimeBaseModel):
    '''User's favorite web'''
    name = models.CharField(max_length=50, verbose_name='站点名称')
    address = models.TextField(verbose_name='站点地址')
    owner = models.ForeignKey(SiteUser, on_delete=models.CASCADE, verbose_name='用户')

    def __str__(self):
        return self.name

    @property
    def data(self):
        data = model_to_dict(self)
        return data

    def get_data(self):
        return {
            'name': self.name,
            'address': self.address,
            'time_added': self.time_added,
            'owner': self.owner.id,
        }
