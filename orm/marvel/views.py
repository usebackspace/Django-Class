from django.shortcuts import render
from .models import Marvel
# Create your views here.
def ironman(request):
    return render(request, 'marvel/ironman.html',{'villian':'Thanos'})

def spiderman(request):
    marvel = Marvel.objects.all()
    print(marvel.query)
    return render(request, 'marvel/spiderman.html',{'marv':marvel})
