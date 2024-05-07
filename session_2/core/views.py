from django.shortcuts import render

def settestcookie(request):
    request.session.set_test_cookie()
    return render(request,'core/settestcookie.html')

def testcookieworked(request):
    request.session.test_cookie_worked()
    return render(request,'core/testcookieworked.html')

def deletetestcookie(request): 
    request.session.delete_test_cookie()
    return render(request,'core/deletetestcookie.html')