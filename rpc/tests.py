#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import unittest

from users_client import UserClient


class TestRPCMethods(unittest.TestCase):
    def setUp(self):
        self.client = UserClient()
        print('Client ready')

    def tearDown(self):
        print('Test finished')

    '''
    def test_user_register(self):
        username = 'rpc_user2'
        password = 'password'
        login_type = 0

        res = self.client.register(
            login_type,
            username=username,
            password=password
        )
        print(res)
        self.assertTrue(res['success'])

    def test_exist_user(self):
        username = 'rpc_user2'
        password = 'password'
        login_type = 0

        res = self.client.register(
            login_type,
            username=username,
            password=password
        )
        print(res)
        self.assertFalse(res['success'])

    def test_user_login(self):
        username = 'rpc_user2'
        password = 'password'
        login_type = 0

        res = self.client.login(
            login_type,
            username=username,
            password=password
        )
        print(res)
        self.assertTrue(res['success'])

    def test_wrong_user_login(self):
        username = 'wrong'
        password = 'password'
        login_type = 0

        res = self.client.login(
            login_type,
            username=username,
            password=password
        )
        print(res)
        self.assertFalse(res['success'])

    def test_wrong_password_login(self):
        username = 'rpc_user1'
        password = 'wrong'
        login_type = 0

        res = self.client.login(
            login_type,
            username=username,
            password=password
        )
        print(res)
        self.assertFalse(res['success'])
    '''

    def test_get_user_info(self):
        user_id = 81
        res = self.client.get_user_info(user_id)
        print(res)
        self.assertTrue(res['success'])

    def test_wrong_id(self):
        user_id = 9999
        res = self.client.get_user_info(user_id)
        print(res)
        self.assertTrue(res['success'])


if __name__ == '__main__':
    unittest.main()
