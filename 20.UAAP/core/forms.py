from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class SignupForm(UserCreationForm):
    class Meta:
        model =User
        fields =['username','first_name','last_name']


class UserProfileForm(UserChangeForm):
    password =None
    class Meta:
        model = User
        fields =['username','first_name','last_name','email','date_joined','last_login']
        

class AdminProfileForm(UserChangeForm):
    password =None
    class Meta:
        model = User
        fields = '__all__'
        