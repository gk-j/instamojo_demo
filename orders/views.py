import requests
import base64
from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.http import JsonResponse
import json
# Create your views here.
from instamojo_wrapper import Instamojo
from django.conf import settings
api = Instamojo(api_key=settings.API_KEY,
                auth_token=settings.AUTH_TOKEN, endpoint='https://test.instamojo.com/api/1.1/')


def home_view(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


def order_page(request,product_id):
    try:
        product_obj = Product.objects.get(uid=product_id)
        order_obj, _ = Order.objects.get_or_create(
            product=product_obj,
            user=request.user,
            is_paid=False
        )
        print("Order Object:", order_obj)
        response = api.payment_request_create(
            amount=order_obj.product.product_price,
            purpose='Order process',
            buyer_name='Gokul',
            email="foo@example.com",
            redirect_url="http://127.0.0.1:8000/order-success"
        )
        # print(response)
        order_obj.order_id = response['payment_request']['id']
        order_obj.instamojo_response=response

        order_obj.save()

        context = {
            'payment_url': response['payment_request']['longurl']
        }
        return render(request, 'order.html', context=context)
    except Exception as e:
        print(e)


def order_success(request):
    payment_request_id = request.GET.get('payment_request_id')
    order_obj = Order.objects.get(order_id= payment_request_id)
    response = api.payment_request_status(payment_request_id)
    order_obj.instamojo_response = response
    if response['payment_request']['status'] == "Completed":
        order_obj.is_paid = True
        order_obj.save()
        return HttpResponse('Payment Success')

    else:
        try:
            failure = response['payment_request']['payments'][0]['failure']
            # print({'failure' : failure})
            order_obj.save()
            return HttpResponse(failure['reason'])
        except IndexError:
            order_obj.save()
            return HttpResponse('Payment Pending')


