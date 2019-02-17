#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import sys
import asyncio

import pytest
import django

BASE_DIR = os.path.dirname(os.path.dirname(__name__))
sys.path.append(BASE_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'meetpencil.settings'

django.setup()

from django.contrib.auth.models import User
import pymysql

from users.models import SiteUser, AccountUser
from users.handler import SiteUserHandler
from guide.models import Favorite


class TestUser:
    def setup(self):
        print('User test begin')
        self.username = 'testuser3'
        self.password = 'testpassword3'
        self.email = 'test@test'
        self.first_name = 'first'
        self.last_name = 'last'
        self.phone = '17781380212'

    def test_account_a_register(self):
        res = SiteUserHandler.register(
            login_type=0,
            username=self.username,
            password=self.password,
            email=self.email,
            first_name=self.first_name,
            last_name=self.last_name,
            phone=self.phone
        )
        print(res)
        assert bool(res)

    def test_b_login(self):
        res = SiteUserHandler.login(
            login_type=0,
            username=self.username,
            password=self.password
        )
        print(res)
        assert bool(res)

    def test_d_logout(self):
        pass

    def teardown(self):
        print('User test finished')


class UserTrans:
    def __init__(self):
        self.connect = pymysql.connect(
            host='localhost',
            user='pencil',
            password='hummel165',
            database='meetpencil'
        )

    @staticmethod
    def get_django_user():
        return User.objects.all()

    @staticmethod
    async def create_site_user(django_user):
        site_user = SiteUser.objects.create(login_type=0)
        AccountUser.objects.create(
            site_user=site_user,
            django_user=django_user
        )
        return site_user

    @staticmethod
    async def change_owner(django_user, site_user):
        Favorite.objects.filter(owner__id=django_user.id).update(owner=site_user)
        print('完成')
        return 1

    @staticmethod
    async def trans_task(django_user):
        site_user = await UserTrans.create_site_user(django_user)
        # await UserTrans.change_owner(django_user, site_user)

    @staticmethod
    def trans():
        tasks = []
        django_users = UserTrans.get_django_user()
        for u in django_users:
            coroutine = UserTrans.trans_task(u)
            task = asyncio.ensure_future(coroutine)
            tasks.append(task)

        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.wait(tasks))
        loop.close()

    @staticmethod
    def single_test():
        tasks = []
        u = UserTrans.get_django_user()[0]

        coroutine = UserTrans.trans_task(u)
        task = asyncio.ensure_future(coroutine)
        tasks.append(task)

        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.wait(tasks))
        loop.close()
