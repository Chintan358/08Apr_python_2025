
from django.urls import path,include
from myapp.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    
    path("",index,name="index"),

    # create path for accounts, cart, checkout, compare, details,login-register,shop,wishlist
    path("accounts",accounts,name="accounts"),
    path("cart",cart,name="cart"),
    path("checkout",checkout,name="checkout"),
    path("compare",compare,name="compare"),
    path("details",details,name="details"),
    path("login-register",login_register,name="login_register"),
    path("shop",shop,name="shop"),
    path("wishlist",wishlist,name="wishlist"),
    # create path for search

    path("userReg",userReg,name="userReg"),
    path("userLogin",userLogin,name="userLogin"),
    path("userLogout",userLogout,name="userLogout"),

    path("addtocart",addtocart,name="addtocart"),
    path("deletecart",deletecart,name="deletecart"),
    path("changeqty",changeqty,name="changeqty"),

    path("address",address,name="address"),
    path("get-address",get_address,name="get-address"),

     path("pay",pay,name="pay"),

     path("makeorder",makeorder,name="makeorder")
      
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
