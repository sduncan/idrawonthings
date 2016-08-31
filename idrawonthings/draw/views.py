from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, Kristen. This is your drawing index.")


