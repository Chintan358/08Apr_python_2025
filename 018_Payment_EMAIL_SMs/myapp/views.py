from django.shortcuts import render,HttpResponse
import razorpay
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
import requests
import json




def index(request):
    return render(request,'index.html')

def pay(request):

    amt = int(request.GET['amt'])
    client = razorpay.Client(auth=("rzp_test_6T4aCyCyT7g7Ye", "UQrxO31xR8FIAw6U1mA0DO2i"))

    data = { "amount": amt*100, "currency": "INR", "receipt": "order_rcptid_11" }
    payment = client.order.create(data=data) 
   
    return JsonResponse(payment)


def send_simple_email(request):
        send_mail(
            "Test mail",
            "Testing",
            settings.EMAIL_HOST_USER,  # Sender's email
            ["chintan.tops@gmail.com"],            # List of recipient emails
            fail_silently=False, 
            html_message ='<h1>Hello</h1>'     
        )
        return HttpResponse("mail sent")


def send_sms(request):
     
    url = "https://www.fast2sms.com/dev/bulkV2"

    querystring = {"authorization":"WXfAe5cjnlMG0thTkdLD9IsgRyZbS7w41UzP3H8mKiqQNVEova9vDJtywEXpMNoUieOfPlq1r8HhdnTL","message":"This is test message","language":"english","route":"q","numbers":"7096980289"}

    headers = {
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
    return HttpResponse(response.text)


def get_products(request):
     
     url ="https://fakestoreapi.com/products"

     data = requests.get(url)
     
     return render(request,'product.html',{"products":data.json()})