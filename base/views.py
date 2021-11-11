from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Funation base view


def home(request):
    return HttpResponse('Home Page')


def room(request):
    return HttpResponse('Room')
