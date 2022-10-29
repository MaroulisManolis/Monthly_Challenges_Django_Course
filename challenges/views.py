from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def january(request):
    return HttpResponse("Start learning Django!")


def february(request):
    return HttpResponse("Walk for at least 20 minutes every day!")
