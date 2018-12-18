from django.db import models
from django.contrib.auth.models import User

from .base import TimeBaseModel, SubUserAbstract


class SubUserManager(models.Model):
    login_type = models.SmallIntergerField(choices=LOGIN_TYPE)

    def __init__(self, login_type):
        pass


class User(models.Model):
    '''站点用户'''
    sub_user_manager = models.OneToOneField(SubUserManager)

    


    def login(self):
        self.sub_user.login()


class AccountUser(SubUserAbstract, User):
    sub_user_manager = models.OneToOneField(SubUserManager, related_name='sub_user')


class QQUser(SubUserAbstract):
    def login(self):
        pass


class WechatUser(SubUserAbstract):
    def login(self):
        pass
