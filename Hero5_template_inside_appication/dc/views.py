from django.shortcuts import render

# Create your views here.
def superman(request):
    return render(request, 'dc/superman.html')

def batman(request):
    return render(request, 'dc/batman.html')
