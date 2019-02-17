#! /usr/bin/env python3
# -*- coding:utf-8 -*-

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout

from .interface import AbstractUserFactory
from .models.models import (
    SiteUser, AccountUser, WeiboUser,
    WechatUser, PhoneUser
)


class AccountUserFactory(AbstractUserFactory):
    '''
    login type = 0
    不限于生产对象
    '''
    def create(self, **user_info):
        '''
        注册账号密码新用户
        返回注册成功标志和信息
        '''
        username = user_info.get('username')
        password = user_info.get('password')
        if not all((username, password)):
            raise ValueError('Need username and password')
        if not self._check_username(username):
            # 错误提示 HIND 0 用户名已存在
            return False, 0

        email = user_info.get('email', '')
        first_name = user_info.get('first_name', '')
        last_name = user_info.get('lastname', '')
        phone = user_info.get('phone', '')
        if phone:
            if not self._check_phone(phone):
                # 错误提示 HIND 1 号码不合法
                return False, 1

        django_user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name,
        )
        site_user = SiteUser.objects.create(login_type=0, phone=phone)
        AccountUser.objects.create(
            site_user=site_user,
            django_user=django_user
        )
        return True, site_user.data

    def login(self, **login_info):
        '''
        账号密码登陆
        返回登陆成功标志和信息
        '''
        username = login_info.get('username')
        password = login_info.get('password')
        if not all((username, password)):
            raise ValueError('Need username and password')

        user = authenticate(username=username, password=password)
        if user:
            site_user = SiteUser.objects.get(sub_user__django_user=user)
            site_user.last_login_update()
            return True, site_user.data
        else:
            # 错误提示 HIND 2 用户名或密码不对
            return False, 2

    def logout(self, **logout_info):
        '''
        账号密码登陆
        返回登陆成功标志和信息
        '''
        pass

    def _check_username(self, username):
        '''检查用户名是否被占用'''
        res = not User.objects.filter(username=username).exists()
        return res

    def _check_phone(self, phone):
        '''检查电话是否合法'''
        return True


class WeiboUserFactory(AbstractUserFactory):
    pass


class WechatUserFactory(AbstractUserFactory):
    pass


class PhoneUserFactory(AbstractUserFactory):
    pass
