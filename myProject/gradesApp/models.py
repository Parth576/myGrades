from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    student=models.OneToOneField(User,on_delete=models.CASCADE)
    idno=models.IntegerField(blank=False)
    branch=models.CharField(max_length=256,blank=False)

    def __str__(self):
        return self.student.username

class Teacher(models.Model):
    teacher=models.OneToOneField(User,on_delete=models.CASCADE)
    subject=models.CharField(max_length=256,blank=False)
    phone=models.IntegerField()

    def __str__(self):
        return self.teacher.username



