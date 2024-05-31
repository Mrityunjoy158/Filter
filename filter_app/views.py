from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import StudentSerializer
from .models import Student
from django_filters.rest_framework import DjangoFilterBackend


class StudentAPIView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['city']
    filterset_fields = ['name', 'city']
    # def get_queryset(self):
    #     user = self.request.user
    #     return Student.objects.filter(pass_by=user)
