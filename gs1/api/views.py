from django.shortcuts import render                 #importing the render function from django.shortcuts
from .models import Student                         #importing the Student class from models
from .serializers import StudentSerializer          #importing the StudentSerializer class from serializers.py
from rest_framework.renderers import JSONRenderer   #JSONRenderer is used to convert the data into JSON format
from django.http import HttpResponse , JsonResponse                #importing the HttpResponse class from django.http
# Create your views here.

#Model Object - Single Student Data

def student_detail(request,pk):                       #defining a function student_detail which takes two arguments request and pk
    stu=Student.objects.get(id=pk)                    #getting the student object with the id=pk
    serializer=StudentSerializer(stu)                 #passing the student object to StudentSerializer
    # json_data=JSONRenderer().render(serializer.data)   #converting the data into JSON format
    # return HttpResponse(json_data,content_type='application/json') #returning the JSON data with content type as application/json
    
    return JsonResponse(serializer.data, safe=False)              #returning the JSON data with JSONResponse- alternative to above two lines

#QuerySet - All Student Data

def student_list(request):                            #defining a function student_list which takes one argument request
    stu=Student.objects.all()                         #getting all the student objects
    serializer=StudentSerializer(stu,many=True)       #passing the student objects to StudentSerializer
    json_data=JSONRenderer().render(serializer.data)   #converting the data into JSON format
    return HttpResponse(json_data,content_type='application/json') #returning the JSON data with content type as application/json