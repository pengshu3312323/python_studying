#! /usr/local/env python3
#--coding: utf-8---

from alipay import AliPay   # Import the AliPay SDK
from . import settings      # Import your settings     

def ali_trade_page_pay(params):
    """
    For the 'api_trade_page_pay'
    Input: A dictionary of order parameters.In the dictionary,keys like 'subject','out_trade_no' and 'total_amount' are necessary.   
    Return: A redirect url to pay
    """
    alipay=AliPay(
        appid = settings.pub_params['app_id'],
        app_notify_url=settings.pub_params['app_notify_url'],
        sign_type = settings.pub_params['sign_type'],
        app_private_key_string=settings.pub_params['private_key'],
        alipay_public_key_string=settings.pub_params['alipay_public_key']
        )

    order_string=alipay.api_alipay_trade_page_pay(
        out_trade_no = params['out_trade_no'],
        subject      = params['subject'],
        total_amount = params['total_amount'],
        body         = params['body'],
        return_url   ='http://127.0.0.1:8000/payment/orders/{}/return'.format(params['order_id']),
        ) 

    payment_url=settings.GATEWAY+order_string

    return payment_url

def ali_notify_handler(data):
    '''
    Notification
    Input a dictionary receive from AliPay by method POST
    Return True if payment success
    '''
    alipay=AliPay(
        appid = settings.pub_params['app_id'],
        app_notify_url = settings.pub_params['app_notify_url'],
        sign_type = settings.pub_params['sign_type'],
        app_private_key_string = settings.pub_params['private_key'],
        alipay_public_key_string = settings.pub_params['alipay_public_key'],
        debug = True
        )

    signature = data.pop('sign')
    success = alipay.verify(data,signature)

    if success and data['trade_status'] in ('TRADE_SUCCESS','TRADE_FINISHED'):
        print('trade succeed')
        return True
    else:
        return False

# The func below is not working........
def ali_order_query(out_trade_no):
    '''
    Query the order`s status
    Input:Order`s out_trade_no,which create by seller
    Return:Status of the order
    '''
    alipay=AliPay(
        appid = settings.pub_params['app_id'],
        app_notify_url = settings.pub_params['app_notify_url'],
        sign_type = settings.pub_params['sign_type'],
        app_private_key_string = settings.pub_params['private_key'],
        alipay_public_key_string = settings.pub_params['alipay_public_key'],
        debug = True
    )

    res = alipay.api_alipay_fund_trans_order_query(
             out_biz_no = out_trade_no
             )

    return res
