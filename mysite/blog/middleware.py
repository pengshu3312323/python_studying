#! /usr/local/env python3
#################################################
#--Middleware in Blog--
#
#--Author:Peng Shu
#################################################

import sys

from django.utils.deprecation import MiddlewareMixin
from django.views.debug import technical_500_response
from .models import VisitorNum

class SuperuserDebugMiddleware(MiddlewareMixin):
    '''Only the superuser can see the debug info at exception'''

    def process_exception(self,request,exception):
        if request.user.is_superuser:
            return technical_500_response(request,*sys.exc_info())

class VisitorNumCountMiddleware(MiddlewareMixin):
    '''Count the number of visitors'''

    def process_request(self,request):
        num=VisitorNum.objects.filter(pk=1)
        if len(num)==0:
            new=VisitorNum()
            new.numbers=1
            new.save()
        elif len(num)!=0:
            new=num[0]
            new.numbers+=1
            new.save()
            
