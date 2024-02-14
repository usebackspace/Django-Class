from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.

# def sign_up(request):
#     if request.method == 'POST':
#         mf = UserCreationForm(request.POST)
#         if mf.is_valid():
#             mf.save()
#     else:
#         mf  = UserCreationForm()
#     return render(request,'core/signup.html',{'mf':mf})


def sign_up(request):
    if request.method == 'POST':
        mf = SignupForm(request.POST)
        if mf.is_valid():
            mf.save()
            return redirect('/signup/')    
    else:
        mf  = SignupForm()
    return render(request,'core/signup.html',{'mf':mf})

def log_in(request):
    if not request.user.is_authenticated:  # check whether user is not login ,if so it will show login option
        if request.method == 'POST':       # otherwise it will redirect to the profile page 
            mf = AuthenticationForm(request=request,data=request.POST)
            if mf.is_valid():
                name = mf.cleaned_data['username']
                pas = mf.cleaned_data['password']
                user = authenticate(username=name, password=pas)
                if user is not None:
                    login(request, user)
                    return redirect('/profile/')
        else:
            mf = AuthenticationForm()
        return render(request,'core/login.html',{'mf':mf})
    else:
        return redirect('/profile/')

def profile(request):
    if request.user.is_authenticated:  # This check wheter user is login, if not it will redirect to login page
        return render(request,'core/profile.html',{'name':request.user})
    else:                                                # request.user returns the username
        return redirect('/login/')

def log_out(request):
    logout(request)
    return redirect('/login/')

def profile(request):
    return render(request,'a/profile.html')