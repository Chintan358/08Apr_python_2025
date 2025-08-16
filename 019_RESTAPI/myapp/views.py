from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from myapp.models import *
from myapp.serealizer import *
from rest_framework import status

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



class EmpAPI(APIView):

    def get(self,request):
        try:
            emps = Emp.objects.all()
            ser = EmpSerializer(emps, many=True)
            return Response({"data":ser.data})
        except Exception as e :
            return Response({"errors":"Somethong went wrong"})
    
    def post(self,request):
        try:
            ser = EmpSerializer(data=request.data)
            if not ser.is_valid():
                return Response({"Errors":ser.errors,"message":"something went wrong"},status=status.HTTP_400_BAD_REQUEST)
            else:
                ser.save()
                return Response({"data":ser.data,"message":"Data inserted successfully !!!"},status=status.HTTP_201_CREATED)
        except Exception as e : 
            print(e)
            return Response({"message":"something went wrong"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
       
    def put(self,request):
        try:
            emp= Emp.objects.filter(pk=request.data['id'])
            if not emp:
                return Response({"message":"Id not found"},status=status.HTTP_404_NOT_FOUND)
            ser = EmpSerializer(emp[0], request.data,partial=True)
            if not ser.is_valid():
                  return Response({"Errors":ser.errors,"message":"something went wrong"},status=status.HTTP_400_BAD_REQUEST)
            else:
                ser.save()
                return Response({"data":ser.data,"message":"Data updated successfully !!!"},status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"message":"something went wrong"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

    def delete(self,request):
        try:
            emp= Emp.objects.filter(pk=request.data['id'])
            if not emp:
                return Response({"message":"Id not found"},status=status.HTTP_404_NOT_FOUND)
            emp.delete()
            return Response({"message":"Emp deleted successfully"},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message":"something went wrong"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)