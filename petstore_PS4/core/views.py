from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from . models import Customer,Pet,Order,Cart
from . forms import RegistrationForm,AuthenticateForm,ChangePasswordForm,UserProfileForm,AdminProfileForm,CustomerForm
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.db.models import F

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
        pet = Pet.objects.get(pk=id)

        #------ code for caculate percentage -----
        if pet.discounted_price !=0:    # fetch discount price of particular pet
            percentage = int(((pet.selling_price-pet.discounted_price)/pet.selling_price)*100)
        else:
            percentage = 0
        # ------ code end for caculate percentage ---------
            
        return render(request,'core/pet_details.html',{'pet':pet,'percentage':percentage})


#============================== Registration ==========================================================


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


#============================== Login ==========================================================

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
    

#================================= Profile ====================================================

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


#================================= Logout ====================================================

def log_out(request):
    logout(request)
    return redirect('home')


#================================= Change Password =============================================


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
    

#=========================== Add TO Cart Section =================================================
    
def add_to_cart(request, id):    # This 'id' is coming from 'pet.id' which hold the id of current pet , which is passing through {% url 'addtocart' pet.id %} from pet_detail.html 
    if request.user.is_authenticated:
        product = Pet.objects.get(pk=id) # product variable is holding data of current object which is passed through 'id' from parameter
        user=request.user                # user variable store the current user i.e steveroger
        Cart(user=user,product=product).save()  # In cart model current user i.e steveroger will save in user variable and current pet object will be save in product variable
        return redirect('petdetails', id)       # finally it will redirect to pet_details.html with current object 'id' to display pet after adding to the cart
    else:
        return redirect('login')                # If user is not login it will redirect to login page

def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user)      # cart_items will fetch product of current user, and show product available in the cart of the current user.
    total =0
    delhivery_charge =2000
    for item in cart_items:
        item.product.price_and_quantity_total = item.product.discounted_price * item.quantity
        total += item.product.price_and_quantity_total
    final_price= delhivery_charge + total
    return render(request, 'core/view_cart.html', {'cart_items': cart_items,'total':total,'final_price':final_price})

def add_quantity(request, id):
    product = get_object_or_404(Cart, pk=id)    # If the object is found, it returns the object. If not, it raises an HTTP 404 exception (Http404).
    product.quantity += 1                       # If object found it will be add 1 quantity to the current object   
    product.save()
    return redirect('viewcart')

def delete_quantity(request, id):
    product = get_object_or_404(Cart, pk=id)
    if product.quantity > 1:
        product.quantity -= 1
        product.save() 
    return redirect('viewcart')

def delete_cart(request,id):
    if request.method == 'POST':
        de = Cart.objects.get(pk=id)
        de.delete()
    return redirect('viewcart')

