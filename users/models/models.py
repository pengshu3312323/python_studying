import datetime

from django.forms import model_to_dict
from django.db import models
from django.contrib.auth.models import User

from .base import TimeBaseModel, SubUserAbstractModel, UnsupportedException
from .data import SEX, LOGIN_TYPE


class SiteUser(models.Model):
    '''站点用户'''
    login_type = models.PositiveSmallIntegerField(choices=LOGIN_TYPE)
    phone = models.CharField(max_length=32, blank=True)
    ip = models.CharField(max_length=100, blank=True)
    login_device = models.CharField(max_length=200, blank=True)

    @property
    def sub_user(self):
        # 获取 sub user 对象
        if self.login_type == 0:
            # 账号密码登陆
            sub_user_model = AccountUser
        # elif self.login_type == 1:
        else:
            raise UnsupportedException('login type', self.login_type)

        sub_user = sub_user_model.objects.get(
            site_user=self
        )
        return sub_user

    @property
    def data(self):
        data = model_to_dict(self)
        sub_user = self.sub_user
        sub_user_data = sub_user.data
        data.update(sub_user_data)
        return data

    def last_login_update(self):
        # 更新最近登陆
        now = datetime.datetime.now()
        if self.login_type == 0:
            sub_user = self.sub_user
            sub_user.django_user.last_login = now
            sub_user.django_user.save()
            sub_user.save()
        else:
            raise UnsupportedException('login type', self.login_type)
        return 1


class AccountUser(SubUserAbstractModel):
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

    @property
    def data(self):
        data = model_to_dict(self.django_user, exclude=('password', 'id'))
        data['fullname'] = self.django_user.get_full_name()
        return data


class WeiboUser(SubUserAbstractModel):
    pass


class WechatUser(SubUserAbstractModel):
    pass


class PhoneUser(SubUserAbstractModel):
    pass
