from django.shortcuts import render
from.models import *
from .serializers import *
from rest_framework.renderers import JSONRenderer
from django.http import * 

def studetail(request,x):
    stu = Students.objects.get(id=x) #Complex data in the form of model object
    print(stu)
    ser= StudentSerializer(stu) #Converted into Python obj
    print(ser)
    print(ser.data)
   #jdata=JSONRenderer().render(ser.data)#Converted python obj to json 
    print(jdata)
    # return HttpResponse(jdata,content_type='application/json')
    return JsonResponse(ser.data) #JSONrespnse can be used then we won't have to use line 13 & 15

def stulist(request):
    stu = Students.objects.all()
    print(stu)
    ser= StudentSerializer(stu,many=True) #For serializing all records
    print(ser)
    print(ser.data)
    jdata=JSONRenderer().render(ser.data)#Converted python obj to json 
    print(jdata)
    return HttpResponse(jdata,content_type='application/json')