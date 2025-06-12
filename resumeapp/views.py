from django.shortcuts import render

# Create your views here.

# resumeapp/views.py

from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Smart Resume Analyzer!")
