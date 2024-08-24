from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Cotacao(models.Model):
    moeda_1 = models.CharField(max_length=3)
    moeda_2 = models.CharField(max_length=3)
    conversao = models.CharField(max_length=100, blank=True, null=True)
    valor_venda = models.FloatField(blank=True, null=True)
    valor_compra = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f'{self.conversao}'
    

class ContaBancaria(models.Model):
    saldo_BLR = models.FloatField(blank=True, null=True)
    saldo_USD = models.FloatField(blank=True, null=True)
    saldo_EUR = models.FloatField(blank=True, null=True)
    saldo_BTC = models.FloatField(blank=True, null=True)
    saldo_ARS = models.FloatField(blank=True, null=True)
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)


