from django.shortcuts import render

from rest_framework import generics
from .models import *
from .serializers import *

''' Classroom API views'''
class ListClassroom(generics.ListCreateAPIView):
    serializer_class = ClassroomSeralizer

    def get_queryset(self):
        '''
        class_code - (optional) restricts the returned Classrooms to the one
        with the given six-digit class code
        '''
        queryset = Classroom.objects.all()
        class_code = self.request.query_params.get('class_code', None)

        if class_code is not None:
            queryset = queryset.filter(class_code = class_code)

        return queryset

class DetailClassroom(generics.RetrieveUpdateDestroyAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSeralizer



''' Student API views '''
class ListStudent(generics.ListCreateAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        '''
        student_id - (optional) restricts the returned Students to the one
        with the given nine-digit student ID
        '''
        queryset = Student.objects.all()
        student_id = self.request.query_params.get('student_id', None)

        if student_id is not None:
            queryset = queryset.filter(student_id = student_id)

        return queryset

class DetailStudent(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



''' Attendance transcation API views '''
class ListAttendanceTransaction(generics.ListCreateAPIView):
    serializer_class = AttendanceTransactionSerializer

    def get_queryset(self):
        '''
        classroom - (optional) restricts the returned
        attendance transactions to those associated with the Classroom
        with the given Django ID. [ NOT classroom's class_code!! ]

        class_code - (optional) restricts the returned
        attendance transactions to those associated with the active Classroom
        that currently has the given class code.

        student - (optional) restricts the returned
        attendance transactions to those associated with the Student
        with the given Django ID. [ NOT student's student_id!! ]

        student_id - (optional) restricts the returned
        aatendance transactions to those associated with the Student
        with the given nine-digit student id.

        date - (optional) in form YYYY-MM-DD restricts the returned
        attendance transactions to those that happened on said date.
        '''
        queryset   = AttendanceTransaction.objects.all()

        classroom  = self.request.query_params.get('classroom', None)
        class_code = self.request.query_params.get('class_code', None)

        student    = self.request.query_params.get('student', None)
        student_id = self.request.query_params.get('student_id', None)

        date       = self.request.query_params.get('date', None)

        if classroom is not None:
            queryset = queryset.filter(classroom__id = classroom)

        if class_code is not None:
            queryset = queryset.filter(classroom__class_code = class_code)

        if student is not None:
            queryset = queryset.filter(student__id = student)

        if student_id is not None:
            queryset = queryset.filter(student__student_id = student_id)

        if date is not None:
            queryset = queryset.filter(time__date = date)

        return queryset


class DetailAttendanceTransaction(generics.RetrieveUpdateDestroyAPIView):
    queryset = AttendanceTransaction.objects.all()
    serializer_class = AttendanceTransactionSerializer
