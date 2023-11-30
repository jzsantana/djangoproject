from rest_framework import viewsets
from rest_framework import filters
from Cliente.serializers import DebitCardSerializer, AccountCustomerSerializer, CreditCardSerializer, TransactionSerializer, CustomerSerializer
from Cliente.models import  AccountCustomer, DebitCard, CreditCard, Customer, Transaction
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from decimal import Decimal


# class CustomerViewSet(viewsets.ModelViewSet):
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer
    

class AccountCustomerViewSet(viewsets.ModelViewSet):
    queryset = AccountCustomer.objects.all()
    serializer_class = AccountCustomerSerializer
    

class DebitCardViewSet(viewsets.ModelViewSet):
    queryset = DebitCard.objects.all()
    serializer_class = DebitCardSerializer
    

class CreditCardViewSet(viewsets.ModelViewSet):
    queryset = CreditCard.objects.all()
    serializer_class = CreditCardSerializer
    

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
                
                # update_saldo_deposito(conta_sender, conta_received, valor)
                
                conta_received.saldo += transaction.valor
                conta_sender.saldo.save()
                conta_received.saldo.save()
                
                return JsonResponse({'message': 'Deposito realizado com sucesso.'})
        
            return JsonResponse({'message': 'Transação realizada com sucesso.'})
        except ValueError as v:
            return JsonResponse({'erro': f'{v}',})
        
    