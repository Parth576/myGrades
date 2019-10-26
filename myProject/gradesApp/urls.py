from django.urls import path
from gradesApp import views

urlpatterns = [
    path('',views.index,name='index'),
]
