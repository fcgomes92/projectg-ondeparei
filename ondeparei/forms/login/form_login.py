__author__ = 'gomes'

from django import forms


class LoginForm(forms.Form):
    email = forms.CharField(label="Email", max_length=254, required=True)
    password = forms.CharField(label="Password", widget=forms.PasswordInput, required=True)
