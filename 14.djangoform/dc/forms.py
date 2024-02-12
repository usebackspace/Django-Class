from django import forms
from .models import DcModel


class DcForm(forms.Form):
    name =forms.CharField()
    heroic_name = forms.CharField()