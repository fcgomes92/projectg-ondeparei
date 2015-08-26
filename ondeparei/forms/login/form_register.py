__author__ = 'gomes'

from django import forms


class RegisterRequestForm(forms.Form):
    email = forms.EmailField(label='Email', required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)
    first_name = forms.CharField(label='First Name', max_length=128, required=True)
    last_name = forms.CharField(label='Last Name', max_length=128, required=True)
    bday = forms.DateField(label='Birthday', widget=forms.DateInput(format='%d/%m/%Y'),
                           input_formats=['%d/%m/%Y', '%Y/%m/%d', ])
