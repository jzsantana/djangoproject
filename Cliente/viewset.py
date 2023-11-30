from rest_framework import viewsets, status
from rest_framework import filters
from Cliente.serializers import DebitCardSerializer, AccountCustomerSerializer, CreditCardSerializer, TransactionSerializer, CustomerSerializer
from Cliente.models import  AccountCustomer, DebitCard, CreditCard, Customer, Transaction, SorteioUnico
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from decimal import Decimal
from rest_framework.response import Response
import random


class AccountCustomerViewSet(viewsets.ModelViewSet):
    queryset = AccountCustomer.objects.all()
    serializer_class = AccountCustomerSerializer
    

class DebitCardViewSet(viewsets.ModelViewSet):
    queryset = DebitCard.objects.all()
    serializer_class = DebitCardSerializer
    

class CreditCardViewSet(viewsets.ModelViewSet):
    queryset = CreditCard.objects.all()
    serializer_class = CreditCardSerializer
    
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
        Decimal(limite)
        
        if conta_cliente.saldo >= 1100:
            CreditCard.objects.create(
                credit_card_number = num_cartao_credito,
                id_cliente_conta = conta_cliente,
                credit_password = senha_credito,
                limite = limite,
                active = True,
                credit_cvv = cvv_credito
            )
            
    
    def get(self, request, credit_card_id=None):
        if credit_card_id is None:
            credit_cards = get_object_or_404(CreditCard, id=credit_card_id)
            serializer = CreditCardSerializer(credit_cards)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            transaction = Transaction.objects.all()
            serializer = TransactionSerializer(transaction, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    
    def create(self, request):
        try:
            print('postei')
            transaction = request.data
            valor = Decimal(transaction["valor"])
            type_transaction = transaction["transaction_type"]       
            
            conta_sender_id = transaction["id_cliente"]
            conta_sender = AccountCustomer.objects.get(id=conta_sender_id)
            conta_receiver_id = transaction["conta_receiver"]
            conta_received = AccountCustomer.objects.get(id=conta_receiver_id)

            # if conta_sender.saldo < valor:
            #      return JsonResponse({'error': "Saldo insuficiente para realizar a transação"}, status=400)
            
            if type_transaction in ["PIX", "TRANSFERENCIA"]:
                Transaction.objects.create(
                    id_cliente=conta_sender,
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
                    conta_received = conta_sender
                )
                
                conta_received.saldo += transaction.valor
                conta_sender.saldo.save()
                conta_received.saldo.save()
                
                return JsonResponse({'message': 'Deposito realizado com sucesso.'})
        
            return JsonResponse({'message': 'Transação realizada com sucesso.'})
        except ValueError as v:
            return JsonResponse({'erro': f'{v}',})
        
    def get(self, request, transaction_id=None):
        if transaction_id is not None:
            transactions = get_object_or_404(Transaction, id=transaction_id)
            serializer = TransactionSerializer(transactions)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            transaction = Transaction.objects.all()
            serializer = TransactionSerializer(transaction, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        
    