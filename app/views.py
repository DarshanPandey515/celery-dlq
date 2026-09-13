from django.shortcuts import render
from app.models import Student, Teacher
from django.http import HttpResponse





def test(request):
    
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    
    print(students)
    print(teachers)
    
    return HttpResponse(students)