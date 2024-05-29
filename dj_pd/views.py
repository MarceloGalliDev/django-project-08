
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def home_view(request):
    return render(request, 'home.html', {})
