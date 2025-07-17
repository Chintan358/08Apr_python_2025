from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,"index.html")

@login_required(login_url="login_register")
def accounts(request):
    return render(request,"accounts.html")

@login_required(login_url="login_register")
def cart(request):
    return render(request,"cart.html")

@login_required(login_url="login_register")
def checkout(request):
    return render(request,"checkout.html")

def compare(request):
    return render(request,"compare.html") 
  
def details(request,id):
    return render(request,"details.html",{"id":id})

def login_register(request):
    return render(request,"login-register.html")
def shop(request):
    return render(request,"shop.html")

@login_required(login_url="login_register")
def wishlist(request):
    return render(request,"wishlist.html")



def userReg(request):
    try : 
        if request.method=='POST':
            data = request.POST
            username = data.get("username")
            email = data.get("email")
            password = data.get("password")

            u = User(username=username,email=email)
            u.set_password(password)
            u.save()
            return render(request,"login-register.html",{"rmessage":"Registration successfully"})
    except Exception as e:
            return render(request,"login-register.html",{"rerr":"Something went wrong"})


def userLogin(request):
    try : 
        if request.method=='POST':
            data = request.POST
            username = data.get("username")
            password = data.get("password")

            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect("index")
            else:
                return render(request,"login-register.html",{"lerr":"Invalid credentials"})
    except Exception as e:
            return render(request,"login-register.html",{"lerr":"Something went wrong"})

def userLogout(request):
    logout(request)
    return redirect("index")