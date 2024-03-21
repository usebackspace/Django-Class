from django.shortcuts import render
from datetime import datetime, timedelta
# Create your views here.
def setcookies(request):
    response = render(request,'core/setcookies.html')
    # response.set_cookie('name','Roger')
    # response.set_cookie('name','Roger',max_age=10)
    # response.set_cookie('name','Roger',expires=datetime.utcnow()+timedelta(days=3))
    response.set_signed_cookie('name','Roger',salt='rr')     # For signed cookies
    return response

def getcookies(request):
    # cookie_value = request.COOKIES.get('name')     # No default value set for the cookie, it will show None
    # cookie_value = request.COOKIES.get('name','Currently No Cookies Is There')
    cookie_value = request.get_signed_cookie('name',salt='rr')
    return render(request, 'core/getcookies.html',{'cookie_value':cookie_value})

def deletecookies(request):
    response = render(request,'core/deletecookies.html')
    response.delete_cookie('name')
    return response


