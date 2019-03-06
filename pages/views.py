from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def homePageView(request):
    return HttpResponse('Hello, World!')

def kPageView(request):
    return HttpResponse('k')

def aPageView(request):
    return HttpResponse('a')