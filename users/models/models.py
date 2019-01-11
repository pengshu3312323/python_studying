from django.forms import model_to_dict
from django.db import models
from django.contrib.auth.models import User, UserManager

from .base import TimeBaseModel, SubUserAbstract
from .data import SEX, LOGIN_TYPE


class UnsupportedException(Exception):
    def __init__(self, type=None, value=None):
        if type and value:
            err = '{}: {} is unsupported'.format(type, value)
        else:
            err = 'Unsupported Error'
        super().__init__(self, err)


class SiteUserManager(models.Manager):
    def create_user(self, login_type, **kwargs):
        if login_type == 0:
            user = self.create(login_type=login_type)
            user.save()
            AccountUser.objects.create_user(user, **kwargs)
        else:
            raise UnsupportedException('Login Type', login_type)
        return user


class SiteUser(models.Model):
    '''站点用户'''
    login_type = models.PositiveSmallIntegerField(choices=LOGIN_TYPE)

    objects = SiteUserManager()

    @property
    def sub_user(self):
        return self.sub_user


class AccountUserManager(UserManager):
    '''
    '''
    # FIXME
    def create_user(self, site_user, **kwargs):
        django_user = super().create_user(username, email=None, password=None, **extra_fields)
        sub_user = self.model(site_user=site_user, django_user=django_user)
        sub_user.save(using=self._db)
        return sub_user


class AccountUser(SubUserAbstract, User):
    '''
    通过账号密码登陆的用户
    中间表，连接SiteUser和Django的User
    '''
    site_user = models.OneToOneField(
        SiteUser,
        related_name='sub_user',
        on_delete=models.CASCADE
    )
    django_user = models.OneToOneField(User, on_delete=models.CASCADE)

    objects = AccountUserManager()

    @property
    def to_dict(self):
        data = model_to_dict(self, exclude=('password, '))
        data['fullname'] = self.get_full_name()
        return data


class WeiboUser(SubUserAbstract):
    pass


class WechatUser(SubUserAbstract):
    pass
