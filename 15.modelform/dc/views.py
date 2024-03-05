from django.shortcuts import render
from .forms import DcForm
# Create your views here.
def success(request):
    return render(request,'dc/success.html')

def superman(request):
    if request.method == 'POST':
        dc =DcForm(request.POST)
        if dc.is_valid():
            n= dc.cleaned_data['heroic_name']
            print(n)
            dc.save()
        dc= DcForm()
        
    else:
        dc= DcForm()
    return render(request,'dc/superman.html',{'villian':'Zod','dc':dc})

def batman(request):
    return render(request,'dc/batman.html',{'villian':'Bayne'})