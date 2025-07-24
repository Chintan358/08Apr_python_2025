
from django.urls import path
from myapp.views import *

urlpatterns = [
    
    path("",index,name="index"),
    path("load",load,name="load"),
    path("reg",reg,name="reg"),
    path("deletestudent",deletestudent,name="deletestudent"),
    path("studentbyid",studentbyid,name="studentbyid"),
    path("update",update,name="update"),
    path("search",search,name="search")

]
