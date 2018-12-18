#! /usr/bin/env python3
# -*- coding:utf-8 -*-

from abc import ABCMeta, abstractmethod

from django.db import models


class TimeBaseModel(models.Model):
    time_added = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')

    class Meta:
        abstract = True


class SubUserAbstract(metaclass=ABCMeta):
    pass
