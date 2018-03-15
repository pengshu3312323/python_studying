#################################################################
#---View function for the 'pay' app
#
#
##################################################################
from time import ctime

from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse

from .models import Order
from blog.models import Blog_post
from .ali.alipay import ali_trade_page_pay,ali_notify_handler,ali_order_query

goods_detail_url='blog:post_detail'

@login_required
def order_list(request):
    '''Display all the orders of a user'''
    orders=Order.objects.filter(user=request.user)
    context={'orders':orders}
    return render(request,'pay/orders.html',context)

@login_required
def order_detail(request,order_id):
    '''Display one order info'''
    order=Order.objects.filter(pk=order_id)[0]
    context={'order':order}
    return HttpResponse('This is order {}'.format(order_id))
#    return render(request,'pay/order_detail.html',context)

def checkout(request,post_id):# Treat my post as goods
    ''' 
    Create the order
    method must be POST
    '''
    # for test
    goods_price=12.0
    goods_body='This is for sell'

    if not request.user.is_authenticated:
        return render(request,'users/login_or_register.html')
    else:
        post=Blog_post.objects.filter(pk=post_id)[0]# Treat my post as goods
        subject = post.title
        owner = request.user
        total_amount = goods_price
        trade_no=str(subject)+str(owner.id)+str(ctime()).replace(' ','')
        body=goods_body

        order=Order.objects.create(subject=subject,owner=owner,total_amount=total_amount,trade_no=trade_no,body=body)
        order.save()
        order_id=order.pk

        return HttpResponseRedirect(reverse('pay:order_detail',args=(order_id,)))

@login_required
def pay(request,order_id):
    '''
    Pay for the order

    if request.POST.get('payment_method')=='Alipay':
        pass
    elif request.POST.get('payment_method')=='Weixin':
        pass
    else:
    '''
    order=Order.objects.filter(pk=order_id)[0]

    params=dict()
    params['out_trade_no'] = order.trade_no
    params['subject']      = order.subject
    params['total_amount'] = order.total_amount
    params['body'] = order.body
    params['order_id']=order_id

#    if request.POST.get('payment_method')=='Alipay':
    payment_url = ali_trade_page_pay(params)
#    elif request.POST.get('payment_method')=='Weixin': 
    return HttpResponseRedirect(payment_url)

# The func below is not working............
#@login_required
#def order_query(request,order_id):
    '''Query your order`s status'''
'''    order=Order.objects.filter(pk=order_id)[0]
    trade_no=order.trade_no

    res=ali_order_query(trade_no)
    print(res)

    return HttpResponse('res')
'''

def notify_handler(request):
    ''' Notify of the order payment status'''
    if request.method == 'POST':
        data=request.POST.dict()
        status=ali_notify_handler(data) # Notification Validation
        if status:
            return HttpResponse("success")
        else:
            return HttpResponse ("fail")
    else:
        return HttpResponse ("fail")

def return_handler(request,order_id):
    ''' Return the status of payment'''
    if request.method == 'GET':
        order=Order.objects.filter(pk=order_id)[0]
        tn = request.GET.get('out_trade_no')
        if tn == order.trade_no:
            print('Order:{} finished'.format(tn))
            return HttpResponse("success")
        else:
            return HttpResponse ("fail")
    else:
        return HttpResponse ("fail")

    




