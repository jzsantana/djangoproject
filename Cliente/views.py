from django.shortcuts import render
# from .models import ClienteConta, CartaoCredito
# from .models import Cliente, ClienteConta, CartaoCredito
import random

from django.contrib import messages
from django.db.models.signals import post_save
from django.dispatch import receiver

from Cliente.models import Cliente


from .api.serializers import ClienteSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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


class TudoAPIView(APIView):
    def get(self, request):
        try:
            queryset = Cliente.objects.all()
            serializer = ClienteSerializer(queryset, many=True)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Create your views here.
def criar_cartao_credito(request):
    from .models import ClienteConta, CartaoCredito
    
    sorteio_senha_cartao = SorteioUnico(1000, 9999)
    sorteio_cvv = SorteioUnico(100, 999)
    sorteio_num_cartao = SorteioUnico(1000000000000000, 9999999999999999)
    
    num_cartao_credito = sorteio_num_cartao.sortear_numero()
    senha_credito = sorteio_senha_cartao.sortear_numero()
    cvv_credito = sorteio_cvv.sortear_numero()
    
    conta_cliente = ClienteConta
    limite = conta_cliente.saldo * 0.08
    
    if conta_cliente.saldo >= 1100:
        CartaoCredito.objects.create(
            num_cartao_credito = num_cartao_credito,
            id_cliente_conta = conta_cliente,
            senha_credito = senha_credito,
            limite = limite,
            ativo = True,
            cvv_credito = cvv_credito
        )
    ...
    
    # USAR O DJOSER, UMA FERRAMENTA PARA JWT    
    
    