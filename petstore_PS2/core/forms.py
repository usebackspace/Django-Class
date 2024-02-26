from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model =User
        fields = ['username','first_name','email','password1','password2']
        labels ={'email':'Email'}
        widgets= {'username':forms.TextInput(attrs={'class':'form-control'}),
                  'email':forms.TextInput(attrs={'class':'form-control'}),
                  'first_name':forms.TextInput(attrs={'class':'form-control'}),
                  }
        
class AuthenticateForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))