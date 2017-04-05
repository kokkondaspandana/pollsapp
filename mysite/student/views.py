from django.shortcuts import render
from django.template import loader

# Create your views here.

from django.http import HttpResponse

from .models import Student

def index(request):
	student_objects = Student.objects.all()
	context = {"students": student_objects}
	return render(request, 'student_list.html', context)

def addstudent(request):
	context = {}
	return render(request, 'add_student.html', context)

def newstudent(request):
	student_entered_name = request.GET.get('name')
	Student.objects.create(name=student_entered_name)
	print(student_entered_name)
	context = {}
	return render(request, 'student_list.html', context)


