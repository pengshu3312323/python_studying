Pay the money
=============

针对于 App 'Pay' 的说明
-----------------------

适用环境
--------
Django 2.0,
Python 3,
支付宝最新支付接口(2017-09-01更新)

安装支付宝SDK
-------------
```
pip install python-alipay-sdk --upgrade
```

存放密钥
--------
将App私钥和支付宝公钥以
```
app_private_key.epm
ali_public_key.pem
```
的形式存放在/the/path/your_django_site/pay/ali/keys/下

配置settings.py
---------------
```
pub_params['app_id'] = ''#商户ID
pub_params['sign_type'] = 'RSA2'# RSA 或者 RSA2
pub_params['app_notify_url'] = 'http://127.0.0.1:8000/payment/orders/notify' 默认回调url
pub_params['private_key'] = open('/your_site_path/pay/ali/keys/app_private_key.pem').read() #商户私钥

pub_params['alipay_public_key'] = open('/your_site_path/pay/ali/keys/ali_public_key.pem').read()#支付宝公钥

GATEWAY='https://openapi.alipaydev.com/gateway.do?' #HTTPS请求地址
```


配置URL
-------
在项目根url.py的urlpatterns中包含pay的url配置，如：
```
path('payment/',include('pay.urls',namespace='pay')),

```

和商品url连接，在商品的url配置里添加
```
from pay.views import checkout

-skip-
urlpatterns=[
	...,
	path('your/goods_list/<int:goods_id>/checkout/',checkout),
	...

	]
```
修改视图
--------
在pay/views.py中与商品连接
```
from your_goods_app.models import Your_goods_model

-skip-

def check(request,goods_id): #将参数修改为商品模型id(或者其他你查找它的方式)
	-skip-

	goods_selled=Your_goods_model.objects.filter(pk=goods_id)

```
以此来帮助订单获取商品信息

订单支付
--------
请求 your/site_path/payment/orders/the_order_id_you_wanna_pay/comfirm


