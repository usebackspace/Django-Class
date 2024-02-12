from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request, 'urlform/base.html')

def about(request,id):
    print(id)
    return render(request,'urlform/about.html',{'id':id})