from django import forms

# class Dc(forms.Form):
#     name = forms.CharField(label="Hero Name",label_suffix="  -", required=False   )
#     heroic_name =forms.CharField(widget=forms.TextInput(attrs={'placeholder':'hi'}),error_messages={'required':'dfdfsdfd'} )
#     city =forms.EmailField()


class Dc(forms.Form):
    name = forms.CharField(label='full name',label_suffix='',error_messages={'required':'please do the needful'})
    heroic_name =forms.CharField(help_text='fsd')

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        heroic_name = cleaned_data['heroic_name']


        if len(name)<40:
            raise forms.ValidationError(' Name Less than 40 Character')
        
        if len(heroic_name)<40:
            raise forms.ValidationError(' heroic name Less than 40 Character')
        