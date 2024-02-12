from django import forms
from .models import MarvelModel

class MarvelForm(forms.ModelForm):
    class Meta:
        model = MarvelModel

        fields = ['name','heroic_name']

        widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control name'}),
        'heroic_name': forms.TextInput(attrs={'class': 'form-control heroicname'}),
        # Add more fields as needed
            }
        

        
         