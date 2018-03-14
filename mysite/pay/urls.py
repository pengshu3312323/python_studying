#############################################
#
#--URLConfig of 'pay' app
#
#############################################

from django.urls import path

from django.views.generic import ListView

from . import views
from .models import Order

app_name = 'pay'

urlpatterns=[
#        Display the all to sell
#        path('goods/',views.goods_list,name='goods_list'),
#        Display the detail of the one
#        path('goods/<int:goods_id>/',views.goods_detail,name='goods_detail'),
#        Create an order of the good
#        path('goods/<int:goods_id>/checkout/',views.checkout,name='checkout'),
       # Treat my posts as goods for now
#        Pay the money,last step
#        path('goods/<int:goods_id>/checkout/comfirm/',views.pay,name='pay'), 
        path('orders/',views.order_list,name='order_list'),
        path('orders/<int:order_id>/',views.order_detail,name='order_detail'),
        path('orders/<int:order_id>/comfirm/',views.pay,name='comfirm_to_pay'),
        path('orders/notify/',views.notify_url_handler,name='notify'),
        path('orders/<int:order_id>/return/',views.return_url_handler,name='return'),
        ]
