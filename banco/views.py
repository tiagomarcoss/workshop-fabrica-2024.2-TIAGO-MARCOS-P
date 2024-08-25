from django.shortcuts import render
from .models import *
from .forms import *
import requests
from django.urls import reverse
# Create your views here.

def get_cotacao(request):
    form = CotacaoForm(request.GET or None)
    moeda_1 = None
    moeda_2 = None
    cotacao = None
    if form.is_valid():
        moeda_1 = form.cleaned_data['moeda_1']
        moeda_2 = form.cleaned_data['moeda_2']

        response = requests.get(f'https://economia.awesomeapi.com.br/json/last/{moeda_1}-{moeda_2}')

        if response.status_code == 200:
            dados_api = response.json()
            dados_api = dados_api[f'{moeda_1}{moeda_2}'] #A api externa funciona com um dicionário dentro de outro, entao tenho que acessar chave e valor duas veses
            cotacao = Cotacao.objects.create(
                moeda_1 = moeda_1,
                moeda_2 = moeda_2,
                conversao = dados_api.get('name'),
                valor_venda = dados_api.get('bid'),
                valor_compra = dados_api.get('ask'),
            )
    return render(request, 'banco_g-cotacao.html', {'form':form, 'cotacao':cotacao})

def create_conta_bancaria(request):
    form = ContaBancariaForm()
    if request.method == 'POST':
        form = ContaBancariaForm(request.POST)

        if form.is_valid():
            form.save()
    return render(request, 'banco_c-conta_bancaria.html', {'form':form})

def create_user(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()
    return render(request, 'banco_c-user.html', {'form':form})


def get_conta_bancaria(request, pessoa_id):
    usuario = ContaBancaria.objects.get(pk = pessoa_id)

    return render(request, 'banco_g-conta_bancaria.html', {'usuario':usuario})
 
def delete_conta_bancaria(request, pessoa_id):
    usuario = ContaBancaria.objects.get(pk = pessoa_id)
    usuario.delete()

def update_conta_bancaria(request, pessoa_id):
    usuario = ContaBancaria.objects.get(pk = pessoa_id)
    form_action = reverse('banco:update_conta_bancaria', args=(pessoa_id,))

    form = ContaBancariaForm()
    if request.method == 'POST':
        form = ContaBancariaForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
    return render(request, 'banco_u-conta_bancaria.html', {'form_action':form_action, 'form':ContaBancariaForm(instance=usuario) })