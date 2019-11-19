from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StudentSerializer
from student.models import Student


from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CourseSerializer
from course.models import Course



from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TeacherSerializer
from teacher.models import Teacher





class StudentViewSet(viewsets.ModelViewSet):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer

class CourseViewSet(viewsets.ModelViewSet):
	queryset = Course.objects.all()
	serializer_class = CourseSerializer


class TeacherViewSet(viewsets.ModelViewSet):
	queryset = Teacher.objects.all()
	serializer_class = TeacherSerializer

# Create your views here.
