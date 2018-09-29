#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# Models in the 'guide' app---
# Written by:Peng Shu

from django.db import models
from django.contrib.auth.models import User

from .base import TimeBaseModel


class Favorite(TimeBaseModel):
    '''User's favorite web'''
    name = models.CharField(max_length=50, verbose_name='站点名称')
    address = models.TextField(verbose_name='站点地址')
    time_added = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')

    def __str__(self):
        return self.name
