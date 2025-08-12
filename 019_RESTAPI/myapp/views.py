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