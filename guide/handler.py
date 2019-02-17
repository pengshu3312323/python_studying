#! /usr/bin/env python3
# -*- coding:utf-8 -*-

from guide.models import Favorite
from users.models import SiteUser
from util.cache import CustomCache


class UserFavoriteHandler:
    '''
    favorite增查改删
    以用户为单位
    '''
    def __init__(self, user_id):
        self.user_id = int(user_id)
        try:
            self.user = SiteUser.objects.get(id=self.user_id)
        except SiteUser.DoesNotExist:
            raise ValueError(
                'Can`t find the user whose id is {}'.format(self.user_id)
                )
        self.cache_key = 'favorites_{}'.format(self.user_id)

    def create_favorite(self, name, address):
        '''添加收藏'''
        name = str(name)
        address = str(address)
        if not address.startswith(('http', 'ftp')):
            # Check whether the user add the protocol or not
            address = 'http://' + address

        CustomCache.delete(self.cache_key)

        new = Favorite.objects.create(name=name, address=address, owner=self.user)
        new.save()
        return new.data

    def get_favorite(self, id=None, address=None, name=None, ):
        '''按id, 名称，域名条件查找'''
        if id:
            try:
                site = Favorite.objects.get(id=id)
                return site.data
            except Favorite.DoesNotExist:
                return None
        elif address:
            sites = Favorite.objects.filter(address=address)
            if sites:
                return [s.data for s in sites]
            else:
                return None
        elif name:
            sites = Favorite.objects.filter(name=name)
            if sites:
                return [s.data for s in sites]
            else:
                return None
        else:
            raise ValueError('Need favorite id, name or address')

    def get_favorites(self):
        '''返回该用户的所有favorites'''
        sites_data = CustomCache.get(self.cache_key)
        if not sites_data:
            sites = Favorite.objects.filter(owner=self.user)
            if sites:
                sites_data = [s.data for s in sites]
                CustomCache.set(self.cache_key, sites_data, 60 * 60)
                return sites_data
            else:
                return None
        else:
            return sites_data

    def delete_favorites(self, id=None, ids=[]):
        '''批量删除收藏'''
        CustomCache.delete(self.cache_key)
        count = 0
        ids = list(ids)
        ids.append(id)
        for id in ids:
            try:
                int(id)
                favorite = Favorite.objects.get(id=id)
                favorite.delete()
                count += 1
            except Exception:
                continue
        return count
