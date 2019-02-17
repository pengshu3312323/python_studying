#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import time
from concurrent import futures

import grpc

import test_pb2
import test_pb2_grpc


class EchoHandler(test_pb2_grpc.TestServicer):

    def Echo(self, request, context):
        time.sleep(request.delay)
        return test_pb2.EchoResponse(msg=request.msg, success=True)


def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    test_pb2_grpc.add_TestServicer_to_server(EchoHandler(), server)

    server.add_insecure_port('[::]:50077')
    server.start()
    try:
        print('Server start')
        while True:
            time.sleep(99999)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    server()
