#! /usr/bin/env python3
# -*- coding:utf-8 -*-
from functools import wraps

from django.shortcuts import redirect
from django.urls import reverse

from .models.models import SiteUser
from .models.base import UnsupportedException
from .models.data import HINT
from .factory import AccountUserFactory


class SiteUserHandler:
    @staticmethod
    def register(login_type, **user_info):
        if login_type == 0:
            factory = AccountUserFactory()
        else:
            raise UnsupportedException('login_type', login_type)
        res = factory.create(**user_info)
        return res

    @staticmethod
    def login(login_type, **login_info):
        if login_type == 0:
            factory = AccountUserFactory()
        else:
            raise UnsupportedException('login_type', login_type)
        res = factory.login(**login_info)
        return res

    @staticmethod
    def get_user_info(user_id):
        try:
            site_user = SiteUser.objects.get(id=user_id)
        except SiteUser.DoesNotExist:
            # 错误提示 HIND 3是用户不存在
            return False, 3
        user_data = site_user.data
        return True, user_data


class SiteUserSessionCtr:
    @staticmethod
    def login(request, user_id, username):
        '''登陆后向session设置用户信息'''
        request.session['is_login'] = True
        request.session['user_id'] = user_id
        request.session['username'] = username
        return 1

    @staticmethod
    def login_check(request):
        '''
        检查是否在登陆状态
        如果是，返回用户信息
        如果否，返回False
        '''
        if request.session.get('is_login'):
            user_id = request.session['user_id']
            res = SiteUserHandler.get_user_info(user_id)
            if res[0]:
                return res[-1]
            else:
                raise ValueError(
                    'Can`t find the user whose id is in the user_id in session'
                )
        else:
            return False

    @staticmethod
    def logout(request):
        return request.session.clear()

    @staticmethod
    def login_required_decorator(view_func):
        @wraps(view_func)
        def check(request, *args, **kwargs):
            if request.session['is_login']:
                return view_func(request, request, *args, **kwargs)
            else:
                return redirect(reverse('users:login'))
        return check
