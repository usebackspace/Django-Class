from django.shortcuts import render

# Create your views here.
def setcookies(request):
    response = render(request,'core/setcookies.html')
    response.set_cookie('name','Roger')
    return response

def getcookies(request):
    cookie_value = request.COOKIES.get('name')
    return render(request, 'core/getcookies.html',{'cookie_value':cookie_value})

def deletecookies(request):
    response = render(request,'core/deletecookies.html')
    response.delete_cookie('name')
    return response