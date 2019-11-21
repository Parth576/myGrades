from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    student=models.OneToOneField(User,on_delete=models.CASCADE)
    idno=models.IntegerField(blank=False)
    branch=models.CharField(max_length=256,blank=False)
    is_student=models.BooleanField(default=True)

    def __str__(self):
        return self.student.username

class Teacher(models.Model):
    teacher=models.OneToOneField(User,on_delete=models.CASCADE)
    subject=models.CharField(max_length=256,blank=False)
    phone=models.IntegerField()
    is_student=models.BooleanField(default=False)

    def __str__(self):
        return self.teacher.username

class Grade(models.Model):
    stud=models.ForeignKey(Student,on_delete=models.CASCADE)
    ds=models.IntegerField(null=True,blank=True)
    dld=models.IntegerField(null=True,blank=True)
    dm=models.IntegerField(null=True,blank=True)
    la=models.IntegerField(null=True,blank=True)

    def __str__(self):
        return str(self.stud)



