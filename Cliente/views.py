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
def update_saldo_deposito(instance, instancia,valor):
    instance.saldo += instancia.valor
    instance.save()
        
    return f'update feito'              

class TransactionViewSet(viewsets.ModelViewSet):
    # sender = envia
    # receiver - received - recebe
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def create(self, request):
        try:
            print('postei')
            # conta_sender = get_object_or_404(AccountCustomer, id=request.data.get('id'))
            conta_sender = request.data.get('id_cliente_conta')
            valor = request.data.get('valor')
            type_transaction = request.data.get('transaction_type')
            # conta_received = get_object_or_404(AccountCustomer, id=request.data.get('id'))        
            conta_received = request.data.get('conta_receiver')        
            
            if conta_sender.saldo < valor:
                 return JsonResponse({'error': "Saldo insuficiente para realizar a transação"}, status=400)
            
            if type_transaction in ["PIX", "TRANSFERENCIA"]:
                Transaction.objects.create(
                    id_cliente_conta=conta_sender,
                    valor=valor,
                    transaction_type=type_transaction,
                    conta_receiver=conta_received
                ) 
                
                conta_sender.saldo -= valor
                conta_sender.save()
                conta_received.saldo += valor
                conta_received.save()
                
                return JsonResponse({'message': 'Transferencia realizada com sucesso.'})

            elif type_transaction in ['DEPOSITO']:
                transaction = Transaction.objects.create(
                    id_cliente_conta = conta_sender,
                    valor = valor,
                    transaction_type = type_transaction,
                    conta_receiver = conta_sender
                )
                
                # update_saldo_deposito(conta_sender, conta_received, valor)
                
                conta_received.saldo += transaction.valor
                conta_sender.saldo.save()
                conta_received.saldo.save()
                
                return JsonResponse({'message': 'Deposito realizado com sucesso.'})
        
            return JsonResponse({'message': 'Transação realizada com sucesso.'})
        except ValueError as v:
            return JsonResponse({'erro': f'Nao foi possivel fazer a transação {v}',})
        
        
        # basicamente, se voce passar o id voce pega uma movimentacao especifica, senao ele pega e retorna todas as movimentações
    def get(self, request, transaction_id=None):
        if transaction_id is not None:
            transactions = get_object_or_404(Transaction, id=transaction_id)
            serializer = TransactionSerializer(transactions)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            transaction = Transaction.objects.all()
            serializer = TransactionSerializer(transaction, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    
class CreateCreditCard(APIView):
    def create(self, request):
        sorteio_senha_cartao = SorteioUnico(1000, 9999)
        sorteio_cvv = SorteioUnico(100, 999)
        num_cartao_credito= str(random.randint(1000000000000000, 9999999999999998))
        
        # num_cartao_credito = sorteio_num_cartao.sortear_numero()
        senha_credito = sorteio_senha_cartao.sortear_numero()
        cvv_credito = sorteio_cvv.sortear_numero()
        
        cliente_id = request.data.get('cliente_id')
        conta_cliente = get_object_or_404(AccountCustomer, id=cliente_id)

        limite = cliente_id.saldo * 0.08
        
        if conta_cliente.saldo >= 1100:
            CreditCard.objects.create(
                credit_card_number = num_cartao_credito,
                id_cliente_conta = conta_cliente,
                credit_password = senha_credito,
                limite = limite,
                active = True,
                credit_cvv = cvv_credito
            )


class MakeLoan(APIView):
    def post(self, required):
        ...
    
