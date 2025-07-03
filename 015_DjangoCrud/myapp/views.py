from django.shortcuts import render,redirect
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


def delete(request):
    id =  request.GET['id']
    student = Student.objects.get(id=id)
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

        st.save()
        return redirect("display")


    id =  request.GET['id']
    student = Student.objects.get(id=id)
    return render(request,"update.html",{"student":student})