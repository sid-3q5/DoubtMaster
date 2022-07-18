from asyncio.windows_events import NULL
from operator import mod
from pydoc import describe
from statistics import mode
from django.db import models

import email
from django.forms import CharField
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, null=True)
    gender = models.CharField(max_length=6, choices= [("Male","Male"), ("Female","Female")], null=True)
    faculty = models.CharField(max_length=7, choices= [("Tutor","Tutor"), ('Student',"Student")], null=True)
    country = models.CharField(max_length=30, null=True)
    state = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=100, default = " ")
    
    def __str__(self):
        return self.user.username
    
class Student(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.CharField(max_length=100, default = " ")
    description = models.CharField(max_length=100, default = " ")

    def __str__(self):
        return self.student.username


class Teacher(models.Model):
    teacher = models.OneToOneField(User, on_delete=models.CASCADE) 
    description = models.CharField(max_length=100, default = " ")
    rating = models.IntegerField(default=1)

    def __str__(self):
        return self.teacher.username

class Doubt(models.Model):
    title = models.CharField(max_length=30, null=True)
    description = models.CharField(max_length=200, null=True)
    related = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True)
    answer = models.CharField(max_length=10, choices= [("Answered","Answered"), ("Unanswered","Unanswered")], default='Unanswered')

    def __str__(self): 
        return self.title 