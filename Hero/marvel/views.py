from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def marvel(request):
    return HttpResponse('Spiderman')

def dc(request):
    return HttpResponse('Super-Man')

