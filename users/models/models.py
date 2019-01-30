from django.forms import model_to_dict
from django.db import models
from django.contrib.auth.models import User

from .base import TimeBaseModel, SubUserAbstractModel, UnsupportedException
from .data import SEX, LOGIN_TYPE


class SiteUser(models.Model):
    '''站点用户'''
    login_type = models.PositiveSmallIntegerField(choices=LOGIN_TYPE)
    phone = models.CharField(max_length=32, blank=True)

    @property
    def data(self):
        if self.login_type == 0:
            # 账号密码登陆
            sub_user_model = AccountUser
        # elif self.login_type == 1:
        else:
            raise UnsupportedException('login type', self.login_type)

        sub_user = sub_user_model.objects.get(
            site_user=self
        )
        data = sub_user.data
        data['id'] = self.id
        data['login_type'] = self.login_type
        data['phone'] = self.phone
        return data


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
