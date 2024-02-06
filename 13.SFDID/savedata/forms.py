from django import forms

class MarvelForm(forms.Form):
    name = forms.CharField( max_length=50, required=False)
    heroic_name = forms.CharField(max_length=50, required=False)