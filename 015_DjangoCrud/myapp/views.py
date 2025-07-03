from django.shortcuts import render
from myapp.models import *
# Create your views here.
def index(request):
    return render(request,"index.html")

def reg(request):
    if request.method=='POST':
        data = request.POST
        name = data.get('name')
        email = data.get('email')
        phone =data.get('phone')
        age = data.get('age')
        
        st = Student.objects.create(name=name,email=email,phone=phone,age=age)
        if st:
            return render(request,'index.html',{"msg":"Registration success"})

    return render(request,'index.html')

def display(request):
    allStudents = Student.objects.all()
    return render(request,'display.html',{"students":allStudents})