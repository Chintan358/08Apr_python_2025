from django.shortcuts import render,HttpResponse
from myapp.models import * 
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request,"index.html")

def load(request):
    allStudents = Student.objects.all()
    return JsonResponse({"data":list(allStudents.values())})

def reg(request):
    if request.method=='POST':
        data = request.POST
        name=data.get("name")
        email = data.get("email")
        phone = data.get("phone")
        age = data.get("age")

        Student.objects.create(name=name,email=email,phone=phone,age=age)
        return HttpResponse("Registration success !!!")
    
def deletestudent(request):
    
    student = Student.objects.get(pk=request.GET['sid'])
    student.delete()
    return HttpResponse("Student Deleted !!!!")

def studentbyid(request):
    student = Student.objects.filter(id=request.GET['sid'])
    return JsonResponse({"data":list(student.values())})

def update(request):
    if request.method=='POST':
        data = request.POST
        id = data.get("id")
        name=data.get("name")
        email = data.get("email")
        phone = data.get("phone")
        age = data.get("age")

        student = Student.objects.get(pk=id)
        student.name = name
        student.email = email
        student.phone = phone
        student.age = age
        student.save()
       
        return HttpResponse("Update success !!!")