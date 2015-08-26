__author__ = 'gomes'

from django.forms import ModelForm
from ondeparei.models import Product


class CreateProductRequestForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
