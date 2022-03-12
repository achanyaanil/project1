from django.shortcuts import render
from django.http import HttpResponse

def programs(request):
    return HttpResponse('welcome')

def function1(request):
    return render(request,'index.html')

def function2(request):
    return render(request,'google.html')

def function3(request):
    return render(request,'facebook.html')