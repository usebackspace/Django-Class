from django.shortcuts import render

# Create your views here.
def ironman(request):
    return render(request, 'marvel/ironman.html',{'villian':'Thanos'})

def spiderman(request):
    return render(request, 'marvel/spiderman.html',{'villian':'Goblin'})
