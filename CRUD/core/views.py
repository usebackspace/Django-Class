from django.shortcuts import render,redirect
from .forms import MarvelForm
from .models import MarvelModel
# Create your views here.
def home(request):
    if request.method == 'POST':
        mf =MarvelForm(request.POST)
        if mf.is_valid():
            mf.save()
        mm =MarvelModel.objects.all()        
        mf= MarvelForm()
    else:
        mm =MarvelModel.objects.all()
        mf =MarvelForm()
    return render(request, 'core/home.html',{'mf':mf,'mm':mm})


def delete(request,id):
    if request.method == 'POST':
        de = MarvelModel.objects.get(pk=id)
        de.delete()
    return redirect('/')
    

def update(request,id):
    if request.method == 'POST':
        um = MarvelModel.objects.get(pk=id)
        mf = MarvelForm(request.POST, instance=um)
        if mf.is_valid():
            mf.save()
        mf = MarvelForm()
    else:
        um =MarvelModel.objects.get(pk=id)
        mf =MarvelForm(instance=um)
    return render(request, 'core/update.html',{'mf':mf})