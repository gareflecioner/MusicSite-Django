from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.

def home(request):
    return HttpResponse('Home page')


def musicians(request,author):
    return HttpResponse(f'<h1>Musicians page</h1>{author}</p>')

def albums(request,collection):
    return HttpResponse(f'<h1>Albums page</h1>{collection}</p>')

def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1>Albums page</h1>')



