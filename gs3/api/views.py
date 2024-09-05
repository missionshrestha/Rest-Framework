from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from .models import Student
from .serializer import StudentSerializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def student_api(request):
    """
    API view for handling student data.

    GET request:
    - If an 'id' parameter is provided in the request body, it retrieves the student with that id and returns the serialized data.
    - If no 'id' parameter is provided, it retrieves all students and returns the serialized data.

    POST request:
    - Creates a new student instance with the data provided in the request body.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the serialized data.

    Raises:
        ParseError: If there is an error parsing the JSON data.
        ValidationError: If the serializer data is not valid.
    """

    if request.method == 'GET':
        # Handling GET request

        # Retrieve the JSON data from the request body
        json_data = request.body

        # Create a stream to read the JSON data
        stream = io.BytesIO(json_data)

        # Parse the JSON data into Python data
        python_data = JSONParser().parse(stream)

        # Retrieve the 'id' parameter from the Python data
        id = python_data.get('id', None)

        if id is not None:
            # If 'id' is provided, retrieve the student with that id
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')

        # If 'id' is not provided, retrieve all students
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')


    elif request.method == 'POST':
        # Handling POST request

        # Retrieve the JSON data from the request body
        json_data = request.body

        # Create a stream to read the JSON data
        stream = io.BytesIO(json_data)

        # Parse the JSON data into Python data
        python_data = JSONParser().parse(stream)

        # Create a serializer instance with the Python data
        serializer = StudentSerializer(data=python_data)

        if serializer.is_valid():
            # If the serializer data is valid, save the student instance
            serializer.save()
            res = {'msg':'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        
        # If the serializer data is not valid, return the errors
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
            

        
