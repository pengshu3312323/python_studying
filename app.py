#! /usr/local/env python3
# -*- coding:utf-8 -*-

import os

PORT = 8000


def start():
    cmd = 'python manage.py runserver 0.0.0.0:%d' % (PORT)
    os.system(cmd)


start()
