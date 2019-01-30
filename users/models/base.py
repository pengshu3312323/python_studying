#! /usr/bin/env python3
# -*- coding:utf-8 -*-

from abc import ABCMeta, abstractmethod

from django.db import models


class TimeBaseModel(models.Model):
    time_added = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')

    class Meta:
        abstract = True


class SubUserAbstractModel(models.Model):
    '''
    子用户抽象基类
    规定子用户方法
    '''
    @property
    def data(self):
        pass

    class Meta:
        abstract = True


class UnsupportedException(Exception):
    def __init__(self, type=None, value=None):
        if type and value:
            err = '{}: {} is unsupported'.format(type, value)
        else:
            err = 'Unsupported Error'
        super().__init__(self, err)