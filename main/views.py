from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def loginPage(request):
    context = {}
    return render(request, 'auth/login.html', context)