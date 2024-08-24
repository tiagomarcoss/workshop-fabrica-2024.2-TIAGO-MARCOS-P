from django.shortcuts import render
from .models import *
from .forms import *
import requests
# Create your views here.

def create_cotacao(request):
    form = CotacaoForm()
    if request.method == 'POST':  
        form = CotacaoForm(request.POST)

        if form.is_valid():
            form.save()
    
    return render(request, 'banco.html', {'form':form})

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
            dados_api = dados_api[f'{moeda_1}{moeda_2}'] #A api externa funciona com uum dicionário dentro de outro, entao tenho que acessar chave e valor duas veses
            cotacao = Cotacao.objects.create(
                moeda_1 = moeda_1,
                moeda_2 = moeda_2,
                conversao = dados_api.get('name'),
                valor_venda = dados_api.get('bid'),
                valor_compra = dados_api.get('ask'),
            )
    return render(request, 'banco.html', {'form':form, 'cotacao':cotacao})