from django.shortcuts import render,HttpResponse
from myapp.models import *
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request,"index.html")

def reg(request):
    name = request.GET['name']
    print(name)
    return HttpResponse("success")

def search(request):
    prod  = request.GET['product']
    allproduct =  Product.objects.filter(name__startswith=prod)
    return JsonResponse({"data":list(allproduct.values())})


def countries(request):
    allCountris  =Country.objects.all()
    return JsonResponse({"data":list(allCountris.values())})

def states(request):
    cid = request.GET['cid']
   
    allStates  =State.objects.filter(country=cid)
    return JsonResponse({"data":list(allStates.values())})


def cities(request):
    
    sid = request.GET['sid']
    allcities = City.objects.filter(state=sid)
    return JsonResponse({"data":list(allcities.values())})