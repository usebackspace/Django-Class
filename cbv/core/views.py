from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import CbvForm

# Create your views here.


def fbv(request):
    return HttpResponse('<h1> Function Base View </h1>')


class Cbv(View):
    def get(self,request):
        return HttpResponse('<h1> Class Base View </h1>')
       
def home(request):
    return render(request,'core/home.html')


class Home(View):
    name = ' Tony'
    def get(self,request):
        # return render(request,'core/home.html')
        return HttpResponse(self.name)
   
def form(request):
    if request.method =='POST':
        cbv = CbvForm(request.POST)
        if cbv.is_valid():
            nm = cbv.cleaned_data['name']
            print(nm)
    else:
        cbv =CbvForm()
    return render(request,'core/forms.html',{'cbv':cbv})


class Formcls(View):
    def get(self,request):
        cbv =CbvForm()
        return render(request,'core/forms.html',{'cbv':cbv})
   
    def post(self,request):
        cbv = CbvForm(request.POST)
        if cbv.is_valid():
            nm = cbv.cleaned_data['name']
            print(nm)
        return render(request,'core/forms.html',{'cbv':cbv})
   
def temp(request,template_name):
    return render(request,template_name)


class Tempcl(View):
    template_name = ''
    def get(self,request):
        return render(request,self.template_name)
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import CbvForm

# Create your views here.


def fbv(request):
    return HttpResponse('<h1> Function Base View </h1>')


class Cbv(View):
    def get(self,request):
        return HttpResponse('<h1> Class Base View </h1>')
       
def home(request):
    return render(request,'core/home.html')


class Home(View):
    name = ' Tony'
    def get(self,request):
        # return render(request,'core/home.html')
        return HttpResponse(self.name)
   
def form(request):
    if request.method =='POST':
        cbv = CbvForm(request.POST)
        if cbv.is_valid():
            nm = cbv.cleaned_data['name']
            print(nm)
    else:
        cbv =CbvForm()
    return render(request,'core/forms.html',{'cbv':cbv})


class Formcls(View):
    def get(self,request):
        cbv =CbvForm()
        return render(request,'core/forms.html',{'cbv':cbv})
   
    def post(self,request):
        cbv = CbvForm(request.POST)
        if cbv.is_valid():
            nm = cbv.cleaned_data['name']
            print(nm)
        return render(request,'core/forms.html',{'cbv':cbv})
   
def temp(request,template_name):
    return render(request,template_name)


class Tempcl(View):
    template_name = ''
    def get(self,request):
        return render(request,self.template_name)
