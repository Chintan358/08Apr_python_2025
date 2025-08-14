from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from myapp.models import *
from myapp.serealizer import *

@api_view(['POST'])
def add_data(request):
    print(request.body)
    return Response({"msg":"add data calling"})

@api_view(['GET'])
def view_data(request):
    return Response("get api calling")

@api_view(['PUT'])
def update_data(request,id):
    print(id)
    return Response("put api calling")

@api_view(['DELETE'])
def delete_data(request,id):
    print(id)
    return Response("delete api calling")

@api_view(['GET'])
def get_students(request):
    students = Stduent.objects.all()
    ser = StudentSerializer(students,many=True)
    return Response({"students":ser.data})

@api_view(['POST'])
def set_student(request):

    try :
        ser = StudentSerializer(data=request.data)
        if not ser.is_valid():
            return Response({"Errors":ser.errors,"Message":"Something went wrong !!!"})
        else :
            ser.save()
            return Response({"Data":ser.data,"Message":"Student added successfully !!!"})
    except Exception as e:
        return Response({"message":"something went wrong !!!!"})
    
@api_view(['PUT'])
def update_student(request,id):
    try:
        students = Stduent.objects.get(pk=id)
        ser = StudentSerializer(students,request.data,partial=True)
        if not ser.is_valid():
            return Response({"Errors":ser.errors,"Message":"Something went wrong !!!"})
        else :
            ser.save()
            return Response({"Data":ser.data,"Message":"Student updated successfully !!!"})
        
    except Exception as e :
        return Response({"message":"something went wrong"})
    pass


@api_view(['DELETE'])
def delete_student(request,id):
    try:
        students = Stduent.objects.get(pk=id)
        st = students.delete()
        return Response({"message":"student deleted"})
        
    except Exception as e :
        return Response({"message":"something went wrong"})
    pass