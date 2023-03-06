from django.shortcuts import render
import io
from .models import Student
from rest_framework.parsers import JSONParser
from .seializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
@csrf_exempt
def student_api(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id1 = pythondata.get('id', None)
        if id1 is not None:
            stu = Student.objects.get(id=id1)  
            serializer = StudentSerializer(stu)
            data = JSONRenderer().render(serializer.data)
            return HttpResponse(data, content_type = 'application/json')
    
        student = Student.objects.all()
        serializer = StudentSerializer(student, many = True)
        data = JSONRenderer().render(serializer.data)
        return HttpResponse(data, content_type = 'application/json')
    
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data = pythondata)
        
        if serializer.is_valid:
            serializer.save()
            res = {'msg': 'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type = 'application/json')
        
        json_data = JSONRenderer.render(serializer.errors)
        return HttpResponse(json_data, content_type = 'application/json')
    
    