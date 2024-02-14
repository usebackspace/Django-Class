from django import forms

class MarvelForm(forms.Form):
    name = forms.CharField(help_text="hello how are you")
    heroic_name = forms.CharField()
    city = forms.CharField()
