from django.shortcuts import render
from django.http import HttpResponse


def abc(request):
    return render(request,'home.html')

def deal(request):
    return render(request,'deal.html')

def cart(request):
    return render(request,'cart.html')

def reivew(request):
    return render(request,'reivew.html')

def login(request):
    return render(request,'login.html')

def mi(request):
    return render(request, 'mi.html')
# Create your views here.
