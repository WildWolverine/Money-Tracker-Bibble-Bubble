from django.contrib.auth import authenticate
from django.contrib import messages, auth
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .models import UserProfile


# Create your views here.
def get_home(request):
    return render(request,'home.html')


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        date_of_birth = request.POST['date_of_birth']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'This email is already registered')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email,
                                                password=password1)

                user.save()
                user_profile = UserProfile.objects.create(username=username, date_of_birth=date_of_birth)
                user_profile.save()
                return redirect('login')
        else:
            messages.info(request, "Passwords don't match")
            return redirect('register')
    else:
        return render(request, 'registrationForm.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')