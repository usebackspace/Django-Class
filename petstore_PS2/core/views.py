from django.shortcuts import render,redirect
from django.views import View
from . models import Customer,Pet,Order,Cart
from . forms import RegistrationForm,AuthenticateForm,ChangePasswordForm,UserProfileForm,AdminProfileForm
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash

# Create your views here.
# def home(request):
#     return render(request, 'core/home.html')

# --- Clased Based View of Home ---
class HomeView(View):
    def get(self,request):
        return render(request, 'core/home.html')


def about(request):
    return render(request, 'core/about.html')


def contact(request):
    return render(request, 'core/contact.html')

# --- Function Based View of dog_categories---
# def dog_categories(request):
#     return render(request,'core/dog_categories.html')

#=========================================================================================================

#--- Class Based View of dog_categories ---
class DogCategoriesView(View):
    def get(self,request):
        dog_category = Pet.objects.filter(category='DOG')  # we are using filter function of queryset, that will filter those data whose category belongs to dog
        return render(request,'core/dog_categories.html',{'dog_category':dog_category})


# --- Function Based View of cat_categories---
# def cat_categories(request):
#     return render(request,'core/cat_categories.html')

#--- Class Based View of cat_categories ---
class CatCategoriesView(View):
    def get(self,request):
        cat_category = Pet.objects.filter(category='CAT')  # we are using filter function of queryset, that will filter those data whose category belongs to dog
        return render(request,'core/cat_categories.html',{'cat_category':cat_category})


def bird_categories(request):
    return render(request,'core/bird_categories.html')

#=========================================================================================================
# def pet_details(request):
#     return render(request,'core/pet_details.html')

class PetDetailView(View):
    def get(self,request,id):     # id = It will fetch id of particular pet 
        pet_detail = Pet.objects.get(pk=id)

        #------ code for caculate percentage -----
        if pet_detail.discounted_price !=0:    # fetch discount price of particular pet
            percentage = int(((pet_detail.selling_price-pet_detail.discounted_price)/pet_detail.selling_price)*100)
        else:
            percentage = 0
        # ------ code end for caculate percentage ---------
            
        return render(request,'core/pet_details.html',{'pd':pet_detail,'percentage':percentage})


#=========================================================================================================


def registration(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            mf = RegistrationForm(request.POST)
            if mf.is_valid():
                mf.save()
                return redirect('registration')    
        else:
            mf  = RegistrationForm()
        return render(request,'core/registration.html',{'mf':mf})
    else:
        return redirect('profile')

def log_in(request):
    if not request.user.is_authenticated:  # check whether user is not login ,if so it will show login option
        if request.method == 'POST':       # otherwise it will redirect to the profile page 
            mf = AuthenticateForm(request,request.POST)
            if mf.is_valid():
                name = mf.cleaned_data['username']
                pas = mf.cleaned_data['password']
                user = authenticate(username=name, password=pas)
                if user is not None:
                    login(request, user)
                    return redirect('/')
        else:
            mf = AuthenticateForm()
        return render(request,'core/login.html',{'mf':mf})
    else:
        return redirect('profile')

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
        return redirect('login')

def log_out(request):
    logout(request)
    return redirect('home')


def changepassword(request):                                       # Password Change Form               
    if request.user.is_authenticated:                              # Include old password 
        if request.method == 'POST':                               
            mf =ChangePasswordForm(request.user,request.POST)
            if mf.is_valid():
                mf.save()
                update_session_auth_hash(request,mf.user)
                return redirect('profile')
        else:
            mf = ChangePasswordForm(request.user)
        return render(request,'core/changepassword.html',{'mf':mf})
    else:
        return redirect('login')