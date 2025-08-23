from django.shortcuts import render
from myapp.models import *
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    students = Student.objects.all()

    paginator = Paginator(students, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,"index.html",{"students":page_obj})

def marksheet(request):
    sid = request.GET['sid']
   
    # student = Student.objects.filter(student_id__student_id=sid)
    marks = Marks.objects.filter(student__student_id__student_id=sid)
    print(marks)
    return render(request,'marksheet.html',{"marks":marks})