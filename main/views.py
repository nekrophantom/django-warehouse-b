from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def loginPage(request):
    context = {}
    return render(request, 'auth/login.html', context)


def homePage(request):
    context = {}
    return render(request, 'pages/home.html', context)

def dashboardPage(request):
    context = {}
    return render(request, 'pages/dashboard.html', context)