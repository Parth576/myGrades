from django.shortcuts import render

# Create your views here.

def index(request):
    insert={'text1':'My Grades', 'text2':'My grades are my grades, none of your grades'}
    return render(request,'gradesApp/homepage.html',context=insert)
