from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.
def register(request):
    return render (request,'form.html')

def registerdata(request):
    name=request.POST.get('firstname')
    email=request.POST.get('email')
    lname=request.POST.get('lastname')    
    password=request.POST.get('password')
    Studentmodel.objects.create(Name=name,Email=email,Lastname=lname,Password=password)
    return HttpResponse("data saves succesfully")
    
