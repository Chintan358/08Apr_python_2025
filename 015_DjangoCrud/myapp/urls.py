
from django.urls import path
from myapp.views import *

urlpatterns = [

    path('',index,name="index"),
    path("reg",reg,name="reg"),
    path('display',display,name="display"),
    path('delete',delete,name="delete"),
    path('update',update,name="update")
]
