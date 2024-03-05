from django.shortcuts import render
from .forms import DcForm
from django.http import HttpResponseRedirect
from  .models import DcModel
# Create your views here.
def success(request):
    return render(request,'dc/success.html')


def superman(request):
    if request.method == 'POST':
        dc= DcForm(request.POST)
        if dc.is_valid():
            name = dc.cleaned_data['name']
            heroic_name = dc.cleaned_data['heroic_name']
            print(name)
            print(heroic_name)
            DcModel(name=name,heroic_name=heroic_name).save()
            # return render(request,'dc/success.html',{'villian':'Zod','dc':dc})
            return HttpResponseRedirect('/dc/success/')

    else:
        dc =DcForm()
        
    return render(request,'dc/superman.html',{'villian':'Zod','dc':dc})

def batman(request):
    return render(request,'dc/batman.html',{'villian':'Bayne'})