#! /usr/bin/env  python3
# -*- coding:utf-8 -*-

import logging
import time

import grpc

import users_pb2
import users_pb2_grpc


class UserClient:
    def __init__(self, host='localhost', port=51210):
        self.stub = self._connect(host, port)

    def _connect(self, host, port):
        channel = grpc.insecure_channel(
            '{}:{}'.format(host, port)
        )
        return users_pb2_grpc.UsersStub(channel)

    def _response_to_dict(self, response):
        # Grpc Response 对象转换成 dict
        res = dict()
        res['success'] = response.success
        res['hint'] = response.hint
        res['user_id'] = response.user_id
        res['login_type'] = response.login_type
        res['username'] = response.username
        res['email'] = response.email
        res['phone'] = response.phone
        res['first_name'] = response.first_name
        res['last_name'] = response.last_name
        res['last_login'] = response.last_login
        res['date_joined'] = response.date_joined
        res['fullname'] = response.fullname
        return res

    def register(self, login_type, **register_info):
        if login_type == 0:
            username = register_info.get('username')
            password = register_info.get('password')
            # TODO 类型检验
            res = self.stub.Register(
                users_pb2.ResgisterLoginRequest(
                    login_type=0,
                    username=username,
                    password=password
                )
            )
            return self._response_to_dict(res)
        else:
            print('只支持login type=0')
            pass

    def login(self, login_type, **login_info):
        if login_type == 0:
            username = login_info.get('username')
            password = login_info.get('password')
            # TODO 类型检验
            res = self.stub.Login(
                users_pb2.ResgisterLoginRequest(
                    login_type=0,
                    username=username,
                    password=password
                )
            )
            return self._response_to_dict(res)
        else:
            print('只支持login type=0')
            pass

    def get_user_info(self, user_id):
        res = self.stub.GetUserInfo(
            users_pb2.GetUserInfoRequest(
                user_id=user_id
            )
        )
        return self._response_to_dict(res)
