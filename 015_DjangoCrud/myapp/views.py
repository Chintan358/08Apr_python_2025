from django.shortcuts import render,redirect
from myapp.models import *
import os
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    alldept = Dept.objects.all()
    return render(request,"index.html",{"depts":alldept})

def reg(request):
    if request.method=='POST':
        data = request.POST
        
        deptid = data.get('dept')
        name = data.get('name')
        email = data.get('email')
        phone =data.get('phone')
        age = data.get('age')
        img = request.FILES['file']
        dept = Dept.objects.get(pk=deptid)

        
        st = Student.objects.create(name=name,email=email,phone=phone,age=age,img=img,dept=dept)
        if st:
           # return render(request,'index.html',{"msg":"Registration success"})
           return redirect("index")

    return render(request,'index.html')

def display(request):
    allStudents = Student.objects.all()
    return render(request,'display.html',{"students":allStudents})


def delete(request):
    id =  request.GET['id']
    student = Student.objects.get(id=id)
    os.remove(f"media/{student.img}")
    student.delete()
    return redirect("display")

def update(request):
    if request.method=="POST":
        data = request.POST
        id = data.get('id')
        name = data.get('name')
        email = data.get('email')
        phone =data.get('phone')
        age = data.get('age')
       
       
            
        
        st = Student.objects.get(id=id)
        st.name = name
        st.email =email
        st.phone = phone
        st.age = age
        if request.FILES:
            os.remove(f"media/{st.img}")
            st.img=request.FILES['file']
            


        st.save()
        return redirect("display")


    id =  request.GET['id']
    student = Student.objects.get(id=id)
    return render(request,"update.html",{"student":student})



def user_login(request):
    return render(request,"login.html")

def user_reg(request):
    if request.method=='POST':
        data = request.POST
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        username = data.get('username')
        password = data.get('password')

        u = User(first_name=first_name,last_name=last_name,username=username,email=email)
        u.set_password(password)
        u.save()


    return render(request,"reg.html ")