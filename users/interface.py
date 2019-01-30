#! /usr/bin/env python3
# -*- coding:utf-8 -*-

from abc import ABCMeta, abstractmethod


class AbstractUserFactory(metaclass=ABCMeta):
    @abstractmethod
    def create(self, **user_info):
        pass

    @abstractmethod
    def login(self, **login_info):
        pass
