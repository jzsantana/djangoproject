from django.shortcuts import render
# from .models import ClienteConta, Cliente
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
            raise ValueError
        
        numero_sorteado = random.choice(list(self.range))
        self.range.remove(numero_sorteado)
        return numero_sorteado

# Create your views here.
def criar_cartao_credito():
    ...
    
    # USAR O DJOSER, UMA FERRAMENTA PARA JWT    
    
    