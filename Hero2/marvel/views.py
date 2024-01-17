from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def spiderman(request):
    return HttpResponse('I am spider-man')


def ironman(request):
    return HttpResponse('I am ironman')
