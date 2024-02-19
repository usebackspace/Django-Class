from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserChangeForm
from .forms import SignupForm,UserProfileForm,AdminProfileForm
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
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
            mf = AuthenticationForm(request,request.POST)
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
        if request.method == 'POST':
            if request.user.is_superuser == True:
                mf = AdminProfileForm(request.POST,instance=request.user)
            else:
                mf = UserProfileForm(request.POST,instance=request.user)
            if mf.is_valid():
                mf.save()
        else:
            if request.user.is_superuser == True:
                mf = AdminProfileForm(instance=request.user)
            else:
                mf = UserProfileForm(instance=request.user)
        return render(request,'core/profile.html',{'name':request.user,'mf':mf})
    else:                                                # request.user returns the username
        return redirect('/login/')


def log_out(request):
    logout(request)
    return redirect('/login/')


def pcf(request):                                                  # pcf - Password Change Form               
    if request.user.is_authenticated:                              # pcf - Include old password 
        if request.method == 'POST':                               
            mf =PasswordChangeForm(request.user,request.POST)
            if mf.is_valid():
                mf.save()
                update_session_auth_hash(request,mf.user)
                return redirect('/profile/')
        else:
            mf = PasswordChangeForm(request.user)
        return render(request,'core/pcf.html',{'mf':mf})
    else:
        return redirect('/login/')
    
    
def spf(request):                                                    # spf - set password form
    if request.user.is_authenticated:                                # spf- Doesn't include old password
        if request.method == 'POST':                                 
            mf =SetPasswordForm(request.user,request.POST)
            if mf.is_valid():
                mf.save()
                update_session_auth_hash(request,mf.user)
                return redirect('/profile/')
        else: 
            mf = SetPasswordForm(request.user)
        return render(request,'core/pcf.html',{'mf':mf})
    else:
        return redirect('/login/')
    

