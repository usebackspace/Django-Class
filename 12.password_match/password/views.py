from django.shortcuts import render
from .forms import Password
# Create your views here.
def password(request):

    if request.method == 'POST':
        p =Password(request.POST)
        if p.is_valid():
            name = p.cleaned_data['name']
            password = p.cleaned_data['password']
            re_enter = p.cleaned_data['rpassword']

            print(name)
            print(password)
            print(re_enter)

    else:
        p = Password()
    return render(request, 'password/password.html',{'p':p})