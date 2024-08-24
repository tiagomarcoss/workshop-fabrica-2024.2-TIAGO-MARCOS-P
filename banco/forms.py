from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CotacaoForm(forms.ModelForm):
    class Meta:
        model = Cotacao
        fields = ['moeda_1','moeda_2'] 

class ContaBancariaForm(forms.ModelForm):
    class Meta:
        model = ContaBancaria
        fields = [
    'saldo_BLR', 
    'saldo_USD',
    'saldo_EUR',
    'saldo_BTC',
    'salgo_ARS',
    'pessoa',
]
        
class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2',]