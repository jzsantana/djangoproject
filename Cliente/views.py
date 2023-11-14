from django.shortcuts import render
from .models import ClienteConta, Cliente
import random

from django.db.models.signals import post_save
from django.dispatch import receiver

# from django.contrib.auth.decorators import login_required
# from datetime import datetime

class SorteioUnico:
    def __init__(self, inicio, fim):
        self.range = set(range(inicio, fim + 1))

    def sortear_numero(self):
        if not self.range:
            raise ValueError("Todos os números já foram sorteados")
        
        numero_sorteado = random.choice(list(self.range))
        self.range.remove(numero_sorteado)
        return numero_sorteado

# Create your views here.
@receiver(post_save, sender=Cliente)
def criar_conta(sender, instance, created, **kwargs):
    if created:
        sorteio = SorteioUnico(100000, 999999)
        num_conta = sorteio.sortear_numero()
        
        cliente = Cliente.objects.get(id)
        cliente_conta = ClienteConta.objects.create(
            cliente=instance,
            agencia = '0001',
            num_conta = num_conta,
            senha = senha,
            saldo = 0.0
        )
    
    # post_save.connect(criar_conta, sender=Cliente)
    cliente_conta.save()
    
post_save.connect(criar_conta, sender=Cliente)    
    
    # USAR O DJOSER, UMA FERRAMENTA PARA JWT
    