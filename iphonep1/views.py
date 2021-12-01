from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import PhoneModels
from . import views
from django.contrib.auth.models import User, auth
# Create your views here.
def home(request):
    modles = PhoneModels.objects.all()
    return render(request,"home.html" , {'modles': modles})

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        email = request.POST['email']
        username = request.POST['username']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                return redirect('/')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email taken")
                return redirect('/')
            else:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                user.save();
                messages.info(request, "user created")

        else:
            messages.info(request, "password not matching")
        return redirect('register')
    else:
        return render(request, "home.html")
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
            messages.info(request, 'login successfull')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('/login')

    else:
        return render(request, "home.html")

def logout(request):
    auth.logout(request)
    return redirect('/')