from django.shortcuts import render
from .forms import MarvelForm
# Create your views here.

def x(request):
    mf = MarvelForm()
    return render(request,'core/x.html',{'mf':mf})
