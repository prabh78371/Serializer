from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from flask import request
from .models import Employee
from .serializer import Employeeserilizer
from rest_framework.renderers import JSONRenderer

# Create your views here.
def emp_info(request):
    stu_data = Employee.objects.get(id=1)
    serilizer = Employeeserilizer(stu_data)
    json_data = JSONRenderer().render(serilizer.data)
    return HttpResponse(json_data,content_type = 'application/json')

def emp_detail(request):
    stu_data = Employee.objects.all()
    serilizer = Employeeserilizer(stu_data,many=True)
    return JsonResponse(serilizer.data,safe = False)

