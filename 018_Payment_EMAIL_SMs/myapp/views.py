from django.shortcuts import render,HttpResponse
import razorpay
from django.http import JsonResponse



def index(request):
    return render(request,'index.html')

def pay(request):

    amt = int(request.GET['amt'])
    client = razorpay.Client(auth=("rzp_test_6T4aCyCyT7g7Ye", "UQrxO31xR8FIAw6U1mA0DO2i"))

    data = { "amount": amt*100, "currency": "INR", "receipt": "order_rcptid_11" }
    payment = client.order.create(data=data) 
   
    return JsonResponse(payment)
