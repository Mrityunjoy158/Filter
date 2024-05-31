from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField(unique=True)
    city = models.CharField(max_length=100)
    class_name = models.CharField(max_length=50)
    pass_by = models.CharField(max_length=100, null=True)

    