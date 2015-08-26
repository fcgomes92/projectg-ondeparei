__author__ = 'gomes'

from django.forms import ModelForm
from ondeparei.models import Detail


class CreateProductDetailForm(ModelForm):
    class Meta:
        model = Detail
        fields = '__all__'
