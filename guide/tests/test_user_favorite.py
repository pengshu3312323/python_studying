#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import sys

import pytest
import django

PROJECT_DIR = os.path.dirname(os.path.dirname(__name__))
sys.path.append(PROJECT_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'meetpencil.settings'

django.setup()

from guide.handler import UserFavoriteHandler


favorite_id = None


class TestUserFavorite:
    def setup(self):
        self.user_id = 61
        self.handler = UserFavoriteHandler(61)
        print('-----Start-----')

    def test_create(self):
        name = 'test_name'
        address = 'test_address'

        res = self.handler.create_favorite(name, address)
        print(res)
        favorite_id = res.get('id', None)
        assert bool(res)

    def test_get_favorites(self):
        res = self.handler.get_favorites()
        print(res)
        assert bool(res)

    def test_get_favorite_by_id(self):
        if favorite_id:
            res = self.handler.get_favorite(id=favorite_id)
            print(res)
            assert bool(res)
        else:
            print('No favorite id')
            assert 1 == 1

    def test_get_favorite_by_name(self):
        name = 'test_name'
        res = self.handler.get_favorite(name=name)
        print(res)
        assert bool(res)

    def test_get_favorite_by_address(self):
        address = 'http://test_address'
        res = self.handler.get_favorite(address=address)
        print(res)
        assert bool(res)

    def test_delete_favorites(self):
        ids = [72, 73]
        res = self.handler.delete_favorites(*ids)
        print(res)
        assert bool(res)
