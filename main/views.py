from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import categoryWarehouse, warehouse

# Create your views here.

def loginPage(request):

    page = 'login'

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            admin = User.objects.get(username= username)
        except:
            messages.error(request, 'User does not exist')

        admin = authenticate(request, username=username, password=password)

        if admin is not None:
            login(request, admin)
            return redirect('home')
        else:
            messages.error(request, 'Username or password does not match')


    context = {
        'page' : page
    }

    return render(request, 'auth/login.html', context)

def logoutAdmin(request):
    logout(request)
    return redirect('login')



# Admin Pages
@login_required(login_url= 'login')
def homePage(request):
    context = {}
    return render(request, 'pages/home.html', context)

@login_required(login_url= 'login')
def dashboardPage(request):
    context = {}
    return render(request, 'pages/dashboard.html', context)

@login_required(login_url= 'login')
def categoryWarehousePage(request):
    category = categoryWarehouse.objects.all()

    context = {
        'category' : category,
    }
    return render(request, 'pages/warehouse/category.html', context)