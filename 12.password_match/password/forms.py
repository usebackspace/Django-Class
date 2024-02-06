from django import forms

class Password(forms.Form):
    name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    rpassword = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        rpassword = cleaned_data['rpassword']

        if password != rpassword:
            raise forms.ValidationError('Password Does Not Match ')
