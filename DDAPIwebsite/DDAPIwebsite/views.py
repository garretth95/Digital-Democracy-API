from django.http import HttpResponse
from django.shortcuts import render
from . import templates


def index(request):
    return render(request, 'index.html')


def request_access(request):
    return render(request, "request_access.html")

