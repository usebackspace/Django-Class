from django import forms

class Password(forms.Form):
    name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    rpassword = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data['name']
        password = cleaned_data['password']
        rpassword = cleaned_data['rpassword']

        if name.isnumeric():
            raise forms.ValidationError('Do not enter numbers')

        if password != rpassword:
            raise forms.ValidationError('Password Does Not Match ')
