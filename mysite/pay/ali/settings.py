#---coding:utf-8-----

#公共请求参数

pub_params=dict()

pub_params['app_id'] = '2016091100489608'
pub_params['sign_type'] = 'RSA2'
pub_params['app_notify_url'] = 'http://127.0.0.1:8000/payment/orders/notify'
pub_params['private_key'] = open('/home/pencil/code/py/mysite/pay/ali/keys/app_private_key.pem').read()

pub_params['alipay_public_key'] = open('/home/pencil/code/py/mysite/pay/ali/keys/ali_public_key.pem').read()

GATEWAY='https://openapi.alipaydev.com/gateway.do?'
