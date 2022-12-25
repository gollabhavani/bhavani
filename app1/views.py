from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def bujji(request):
    return HttpResponse('<h1><marquee> this view belongs to bujji</marquee></h1>')