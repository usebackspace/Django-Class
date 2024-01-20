from django.shortcuts import render

# Create your views here.
def ironman(request):
    return render(request, 'ironman.html',{'villian':'Thanos'})

def spiderman(request):
    return render(request, 'spiderman.html',{'villian':'Goblin'})
