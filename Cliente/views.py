# from django.contrib import messages
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .api.serializers import ClienteSerializer
# from django.contrib.auth.decorators import login_required
# from datetime import datetime

from django.shortcuts import render
from Cliente.models import  AccountCustomer, CreditCard, Transaction, SorteioUnico
import random
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.http import JsonResponse

# from rest_framework import serializers
# from Cliente.models import Cliente
from rest_framework import filters
# from Cliente.serializers import ClienteSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from Cliente.serializers import TransactionSerializer


# class ClienteViewSet(viewsets.ModelViewSet):
#     queryset =  Cliente.objects.all()
#     serializer_class = ClienteSerializer


class MakeTransaction(APIView):
    # sender = envia
    # receiver - received - recebe

    def post(self, request):
        conta_sender = get_object_or_404(AccountCustomer, id=request.data.get('id_cliente_conta'))
        valor = request.data.get('valor')
        transaction_type = request.data.get('transaction_type')
        conta_received = get_object_or_404(AccountCustomer, id=request.data.get('conta_receiver'))        
        
        # if conta_sender.saldo < valor:
        #     return JsonResponse({'error': "Saldo insuficiente para realizar a transação"}, status=400)
        
        if Transaction.transaction_type == "PIX" or Transaction.transaction_type == "TRANSFERENCIA":
            transaction = Transaction.objects.create(
                id_cliente_conta=conta_sender,
                valor=valor,
                transaction_type=transaction_type,
                conta_receiver=conta_received
            )
            
            conta_sender.saldo()
            print(conta_sender.saldo)
            
            conta_sender.saldo -= transaction.valor
            conta_received.saldo += transaction.valor
            conta_sender.save()
            conta_received.save()


        elif Transaction.transaction_type == "DEPOSITO":
            transaction = Transaction.objects.create(
                id_cliente_conta = conta_sender,
                valor = float(valor),
                transaction_type = transaction_type,
                conta_receiver = conta_sender
            )
            
            conta_received.saldo += transaction.valor
            conta_sender.save()
            conta_received.save()
            
        return JsonResponse({'message': 'Transação realizada com sucesso.'})
    
    
    # def get(self, request):
    #     transactions = Transaction.objects.all()
    #     serializer = TransactionSerializer(transactions, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)


    def get(self, request, transaction_id=None):
        if transaction_id is not None:
            transaction = get_object_or_404(Transaction, id=transaction_id)
            serializer = TransactionSerializer(transaction)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            transactions = Transaction.objects.all()
            serializer = TransactionSerializer(transactions, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    
    

def criar_cartao_credito(request):
    sorteio_senha_cartao = SorteioUnico(1000, 9999)
    sorteio_cvv = SorteioUnico(100, 999)
    num_cartao_credito= str(random.randint(1000000000000000, 9999999999999998))
    
    # num_cartao_credito = sorteio_num_cartao.sortear_numero()
    senha_credito = sorteio_senha_cartao.sortear_numero()
    cvv_credito = sorteio_cvv.sortear_numero()
    
    conta_cliente = AccountCustomer
    limite = conta_cliente.saldo * 0.08
    
    if conta_cliente.saldo >= 1100:
        CreditCard.objects.create(
            credit_card_number = num_cartao_credito,
            id_cliente_conta = conta_cliente,
            credit_password = senha_credito,
            limite = limite,
            active = True,
            credit_cvv = cvv_credito
        )
    ...
    
    
