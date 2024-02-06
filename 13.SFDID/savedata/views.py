from django.shortcuts import render
from .forms import MarvelForm
from .models import Marvel
# Create your views here.

def marvel(request):
    if request.method == 'POST':
        m= MarvelForm(request.POST)
        if m.is_valid():
            nme = m.cleaned_data['name']
            h_name = m.cleaned_data['heroic_name']
            mm= Marvel(name = nme,heroic_name=h_name)
            mm.save()
    else:
        m = MarvelForm()
    return render(request, 'savedata/marvel.html',{'m':m})