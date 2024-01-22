from django.shortcuts import render

# Create your views here.
def ironman(request):
    return render(request, 'marvel/ironman.html',{'villian':'Thanos'})

def spiderman(request):
    return render(request, 'marvel/spiderman.html',{'villian':'Goblin'})

def villian(request):
    context={'villian':['Goblin','Thanos','Electro','zola','Loki']}
    return render(request, 'marvel/villian loop.html',)