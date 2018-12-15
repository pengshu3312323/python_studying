#! usr/bin/env python3
# -*- coding:utf-8 -*-

from django.http import JsonResponse, HttpResponse, Http404


class Response:
    '''响应处理'''
    @staticmethod
    def success_data():
        return JsonResponse({'code': 1, 'msg': 'Request Success'})

    @staticmethod
    def fail_data():
        return JsonResponse({'code': 0, 'msg': 'Request Fail'})

    @staticmethod
    def error_data(error_msg):
        '''
        返回错误信息
        error_msg --> str
        '''
        return JsonResponse({'code': 0, 'msg': 'Error:{}'.format(error_msg)})

    @staticmethod
    def data(**data):
        '''
        返回成功数据
        data --> dict
        '''
        return_data = {'code': 1, 'msg': 'Request Success'}
        return_data.update(data)
        return JsonResponse(return_data)

    @staticmethod
    def http404():
        '''
        返回404错误
        '''
        raise Http404
