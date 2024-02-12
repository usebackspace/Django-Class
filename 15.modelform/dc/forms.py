from django import forms
from .models import DcModel


class DcForm(forms.ModelForm):
    class Meta:
        model = DcModel
        fields = ['name', 'heroic_name']

        labels = {'name':'Hero Name','heroic_name':'Name of the hero'}

        help_texts = {'name':'Name of the Hero'}

        error_messages = {'name': {'required': 'Enter Name'}, }

        widgets = {
            'name':forms.TextInput(attrs={'placeholder':'Hii','disabled':'disabled'}),
                   }
        
        required = {
            'name': True,   # Make 'name' required
            'heroic_name': True,   # Make 'name' required
            }
        