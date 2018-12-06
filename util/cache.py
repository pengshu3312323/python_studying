#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import random

from django.core.cache import cache


class CustomCache:
    @staticmethod
    def set(key, data, time):
        if not isinstance(key, str):
            raise TypeError('Cache key must be string')
        try:
            time = int(time)
        except Exception:
            raise TypeError('Time must be numbers')

        time = int(time * (10 + random.randint(0, 3)) / 10)

        return cache.set(key, data, time)
