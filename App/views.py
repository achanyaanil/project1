from django.shortcuts import render
from django.http import HttpResponse

def programs(request):
    return HttpResponse('hello')

def function1(request):
    return render(request,'index.html')

def function2(request):
    return render(request,'google.html')