
from django.urls import path
from myapp.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('index',index,name="index"),
    path("reg",reg,name="reg"),
    path('display',display,name="display"),
    path('delete',delete,name="delete"),
    path('update',update,name="update"),

    path("",user_login,name="user-login"),
    path("user-reg",user_reg,name="user-reg"),
    path("user-logout",user_logout,name="user-logout")


    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
