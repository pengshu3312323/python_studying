#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import grpc

import test_pb2
import test_pb2_grpc


class Echo:
    def __init__(self, host='localhost', port=50077):
        self.channel = grpc.insecure_channel(
            "{}:{}".format(host, port)
            )

        self.stub = test_pb2_grpc.TestStub(self.channel)
        print('Connection established')

    def echo(self, msg, delay):
        msg = str(msg)
        delay = int(delay)
        response = self.stub.Echo(test_pb2.EchoRequest(msg=msg, delay=delay))
        return response.success, response.msg


def listen():
    while True:
        msg = input('消息：')
        delay = input('延迟：')
        e = Echo()
        res = e.echo(msg, delay)
        print(res)


if __name__ == '__main__':
    listen()
