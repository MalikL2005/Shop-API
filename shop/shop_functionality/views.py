from django.http import HttpResponse
from rest_framework.response import Response
from django.shortcuts import render, redirect
from .forms import UserForm

def index(request):
    return HttpResponse("Hello, world.")

def home(req):
    return render(req, 'home.html')

def sign_up(req):
    return render(req, 'sign_up.html', {'form': UserForm})

def validate_sign_up(req):
    if req.method == 'POST':
        print(req.POST)
        try:
            new_user = UserForm(req.POST)
            if new_user.is_valid():
                # confirm via Email
                new_user.save()
                print('New User created')
                return redirect('/login')
            else:
                raise ValueError
        except: return HttpResponse("Could not create user")
