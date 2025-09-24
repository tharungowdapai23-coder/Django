from django.http import HttpResponse
from django.shortcuts import render

def home(request):
   #return HttpResponse("hello world")
   return render(request, 'website/index.html')

def hi(request):
   #return HttpResponse("hello world")
   return render(request, 'layout.html')

def about(request):
   return HttpResponse("hello world , you are in about page")