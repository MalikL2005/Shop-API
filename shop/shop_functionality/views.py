from django.http import HttpResponse
from rest_framework.response import Response
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world.")

def home(req):
    return render(req, 'home.html')