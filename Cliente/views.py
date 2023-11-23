# from django.contrib import messages
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .api.serializers import ClienteSerializer
# from django.contrib.auth.decorators import login_required
# from datetime import datetime

from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
from .models import ClienteConta, CartaoCredito,SorteioUnico


from rest_framework import viewsets
# from rest_framework import serializers
from Cliente.models import Cliente
from rest_framework import filters
from Cliente.serializers import ClienteSerializer
# # from django_filters.rest_framework import DjangoFilterBackend


class ClienteViewSet(viewsets.ModelViewSet):
    queryset =  Cliente.objects.all()
    serializer_class = ClienteSerializer
    

def criar_cartao_credito(request):
    sorteio_senha_cartao = SorteioUnico(1000, 9999)
    sorteio_cvv = SorteioUnico(100, 999)
    num_cartao_credito= str(random.randint(1000000000000000, 9999999999999998))
    
    # num_cartao_credito = sorteio_num_cartao.sortear_numero()
    senha_credito = sorteio_senha_cartao.sortear_numero()
    cvv_credito = sorteio_cvv.sortear_numero()
    
    conta_cliente = ClienteConta
    limite = conta_cliente.saldo * 0.08
    
    if conta_cliente.saldo >= 1100:
        CartaoCredito.objects.create(
            credit_card_number = num_cartao_credito,
            id_cliente_conta = conta_cliente,
            credit_password = senha_credito,
            limite = limite,
            active = True,
            credit_cvv = cvv_credito
        )
    ...
    
    
