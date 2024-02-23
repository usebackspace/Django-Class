from django import forms


class CbvForm(forms.Form):
    name = forms.CharField()
    heroic_name = forms.CharField()
