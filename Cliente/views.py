from django.shortcuts import render
from .models import ClienteConta, Cliente
import random

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

def criar_conta(request):
    sorteio = SorteioUnico
    num_conta = sorteio.sortear_numero(100000, 999999)
    
    cliente = Cliente.objects.get(id)
    cliente_conta = ClienteConta.objects.create(
        id_cliente=cliente(id),
        num_conta=num_conta
    )

    
    ...
    
    # USAR O DJOSER, UMA FERRAMENTA PARA JWT
    