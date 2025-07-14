from django.shortcuts import render,redirect
from myapp.models import *
import os
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="user-login")
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

@login_required(login_url="user-login")
def display(request):
    allStudents = Student.objects.all()
    return render(request,'display.html',{"students":allStudents})

@login_required(login_url="user-login")
def delete(request):
    id =  request.GET['id']
    student = Student.objects.get(id=id)
    os.remove(f"media/{student.img}")
    student.delete()
    return redirect("display")

@login_required(login_url="user-login")
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
    try:
        if request.method=='POST':
            data = request.POST
            username = data.get('username')
            password = data.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect("index")
            else : 
                messages.add_message(request, messages.ERROR, "Invalid credentials !!!")
                return render(request,"login.html")
        
    except Exception as e:
        messages.add_message(request, messages.WARNING, "somethinf Went wrong !!! !!!")
        return render(request,"login.html")

    return render(request,"login.html")

def user_reg(request):
    try :
        if request.method=='POST':
            data = request.POST
            first_name = data.get('first_name')
            last_name = data.get('last_name')
            email = data.get('email')
            username = data.get('username')
            password = data.get('password')

            if User.objects.filter(username=username).exists():
                messages.add_message(request, messages.ERROR, "Username already Exist !!!")
                return render(request,"reg.html")

            u = User(first_name=first_name,last_name=last_name,username=username,email=email)
            u.set_password(password)
            u.save()
            messages.add_message(request, messages.SUCCESS, "Registration successfully !!!")
            return render(request,"reg.html")

    except Exception as e:
        messages.add_message(request, messages.WARNING, "somethinf Went wrong !!! !!!")
        return render(request,"reg.html")

    return render(request,"reg.html ")

def user_logout(request):
    logout(request)
    return render(request,"login.html ")