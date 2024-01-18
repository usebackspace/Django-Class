from django.shortcuts import render

# Create your views here.
def ironman(request):
    return render(request, 'ironman.html')

def spiderman(request):
    return render(request, 'spiderman.html')
