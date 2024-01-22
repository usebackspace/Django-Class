from django.shortcuts import render

# Create your views here.
def superman(request):
    return render(request,'superman.html')

def batman(request):
    return render(request,'batman.html')