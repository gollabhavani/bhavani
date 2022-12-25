from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def tharun(request):
    return HttpResponse('<h1><marquee> tharun is innocent boy</marquee></h1>')
