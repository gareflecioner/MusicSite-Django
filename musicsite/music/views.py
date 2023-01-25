from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    posts=Albums.objects.all()
    author=Musicians.objects.all()
    return render(request,'music/home.html',{'posts':posts,'author':author,})


def musicians(request):
    return render(request,'music/musicians.html')

def albums(request):
    return render(request,'music/albums.html')

def about(request):
    return render(request,'music/about.html')

def feedback(request):
    return render(request,'music/feedback.html')

def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1>Ooops...</h1>')



