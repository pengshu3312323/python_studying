#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import sys
import getopt
import time
import datetime
from concurrent.futures import ThreadPoolExecutor

import grpc
import django

import users_pb2
import users_pb2_grpc

BASE_DIR = os.path.dirname(os.path.dirname(__name__))
sys.path.append(BASE_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'meetpencil.settings'
django.setup()

from users.handler import SiteUserHandler


class UserHandler(users_pb2_grpc.UsersServicer):
    @staticmethod
    def _res_format(res):
        if res[0]:
            res = res[1]
            return users_pb2.UserDataResponse(
                success=True,
                user_id=res['id'],
                login_type=res['login_type'],
                username=res['username'],
                phone=res['phone'],
                first_name=res['first_name'],
                last_name=res['last_name'],
                last_login=res['last_login'].strftime('%Y-%m-%d %H:%M:%S') if res['last_login'] else '',
                date_joined=res['date_joined'].strftime('%Y-%m-%d %H:%M:%S'),
                fullname=res['fullname']
            )
        else:
            return users_pb2.UserDataResponse(
                success=False,
                hint=res[1]
                )

    def Register(self, request, context):
        res = SiteUserHandler.register(
            request.login_type,
            username=request.username,
            password=request.password
            )
        return UserHandler._res_format(res)

    def Login(self, request, context):
        res = SiteUserHandler.login(
            request.login_type,
            username=request.username,
            password=request.password
        )
        return UserHandler._res_format(res)

    def GetUserInfo(self, request, context):
        res = SiteUserHandler.get_user_info(
            request.user_id
        )
        return UserHandler._res_format(res)


def server(port=50055):
    # django.setup()
    server = grpc.server(ThreadPoolExecutor(max_workers=8))
    users_pb2_grpc.add_UsersServicer_to_server(UserHandler(), server)

    server.add_insecure_port('[::]:{}'.format(port))
    server.start()

    try:
        print('User grpc server started, listen at port {}'.format(port))
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print('User grpc server stoped')
        server.stop(0)


if __name__ == '__main__':
    opts, _ = getopt.getopt(sys.argv[1:], 'p:', ['port:'])
    port = 51210
    for opt, val in opts:
        if opt == '-p' or opt == '--port':
            try:
                port = int(val)
            except TypeError:
                print('Invalid port')
    server(port=port)
