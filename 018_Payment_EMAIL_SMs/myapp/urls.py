
from django.urls import path
from myapp.views import *
urlpatterns = [
    path("",index,name="index"),

    path("pay",pay,name="pay"),

    path('sendmail',send_simple_email,name="sendmail"),
    path("sendsms",send_sms,name="sendsms"),
    path("products",get_products,name="products")
]
