from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import RegisterForm, LoginForm


def loginview(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
            except KeyError:
                return render(request, 'colorir/login.html', {'error_message': 'Wrong credentials'})
            if user:
                return HttpResponseRedirect(reverse('colorir:home'))
            else:
                return render(request, 'colorir/login.html', {'error_message': 'Wrong credentials'})
    else:
        form = LoginForm()
        return render(request, 'colorir/login.html', {'form': form})


def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('colorir:index'))


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                User.objects.create_user(request.POST['username'], request.POST['email'],
                                         request.POST['password'])
                messages.info(request, "Thanks for registering. You are now logged in.")
                return HttpResponseRedirect(reverse('colorir:login'))
            except KeyError:
                # return render(request, 'colorir/register.html', {'error_message': 'Erro de login'})
                return HttpResponseRedirect(reverse('colorir:register'), {'error_message': 'Error'})

    else:
        form = RegisterForm()
    return render(request, 'colorir/register.html', {'form': form})


def home(request):
    return render(request, 'colorir/home.html')
