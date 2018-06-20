Pay the money
=============

����� App 'Pay' ��˵��
-----------------------

���û���
--------
Django 2.0,
Python 3,
֧��������֧���ӿ�(2017-09-01����)

��װ֧����SDK
-------------
```
pip install python-alipay-sdk --upgrade
```

�����Կ
--------
��App˽Կ��֧������Կ��
```
app_private_key.epm
ali_public_key.pem
```
����ʽ�����/the/path/your_django_site/pay/ali/keys/��

����settings.py
---------------
```
pub_params['app_id'] = ''#�̻�ID
pub_params['sign_type'] = 'RSA2'# RSA ���� RSA2
pub_params['app_notify_url'] = 'http://127.0.0.1:8000/payment/orders/notify' Ĭ�ϻص�url
pub_params['private_key'] = open('/your_site_path/pay/ali/keys/app_private_key.pem').read() #�̻�˽Կ

pub_params['alipay_public_key'] = open('/your_site_path/pay/ali/keys/ali_public_key.pem').read()#֧������Կ

GATEWAY='https://openapi.alipaydev.com/gateway.do?' #HTTPS�����ַ
```


����URL
-------
����Ŀ��url.py��urlpatterns�а���pay��url���ã��磺
```
path('payment/',include('pay.urls',namespace='pay')),

```

����Ʒurl���ӣ�����Ʒ��url���������
```
from pay.views import checkout

-skip-
urlpatterns=[
	...,
	path('your/goods_list/<int:goods_id>/checkout/',checkout),
	...

	]
```
�޸���ͼ
--------
��pay/views.py������Ʒ����
```
from your_goods_app.models import Your_goods_model

-skip-

def check(request,goods_id): #�������޸�Ϊ��Ʒģ��id(����������������ķ�ʽ)
	-skip-

	goods_selled=Your_goods_model.objects.filter(pk=goods_id)

```
�Դ�������������ȡ��Ʒ��Ϣ

����֧��
--------
���� your/site_path/payment/orders/the_order_id_you_wanna_pay/comfirm


