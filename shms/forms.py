from django import forms

class CheckboxForm(forms.Form):
    google = forms.BooleanField(required=False)
    facebook = forms.BooleanField(required=False)
    amazon = forms.BooleanField(required=False)
    twitter = forms.BooleanField(required=False)
    selected_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), input_formats=['%Y-%m-%d'])
    dt = forms.FloatField(required=False, widget=forms.NumberInput(attrs={'min': '0', 'max': '10', 'step': '0.01', 'value': '0.00'}))
