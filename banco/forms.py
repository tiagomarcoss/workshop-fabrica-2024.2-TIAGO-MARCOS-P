from django import forms
from .models import *

class CotacaoForm(forms.ModelForm):
    class Meta:
        model = Cotacao
        fields = ['moeda_1','moeda_2'] 