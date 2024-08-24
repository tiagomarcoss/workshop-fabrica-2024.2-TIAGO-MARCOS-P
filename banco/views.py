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