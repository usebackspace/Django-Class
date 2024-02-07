from django import forms
from .models import DcModel


class DcForm(forms.ModelForm):
    class Meta:
        model = DcModel
        fields = ['name', 'heroic_name']