from rest_framework import viewsets, status
from rest_framework import filters
from Cliente.serializers import DebitCardSerializer, AccountCustomerSerializer, CreditCardSerializer, TransactionSerializer, CustomerSerializer, LoanSerializer
from Cliente.models import  AccountCustomer, DebitCard, CreditCard, Customer, Transaction, SorteioUnico, Loan
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
        print('criando cartão')
        credit = request.data
        conta_cliente_id = credit["id_cliente_conta"]
        conta_cliente = AccountCustomer.objects.get(id=conta_cliente_id)
        
        sorteio_senha_cartao = SorteioUnico(1000, 9999).sortear_numero()
        sorteio_cvv = SorteioUnico(100, 999).sortear_numero()
        num_cartao_credito= str(random.randint(1000000000000000, 9999999999999998))
        
        senha_credito = sorteio_senha_cartao
        cvv_credito = sorteio_cvv
        
        limite_cliente = conta_cliente.saldo
        limite = limite_cliente * 4/10
        
        if conta_cliente.saldo >= 1100:
            CreditCard.objects.create(
                credit_card_number = num_cartao_credito,
                id_cliente_conta = conta_cliente,
                credit_password = senha_credito,
                limite = Decimal(limite),
                active = True,
                credit_cvv = cvv_credito
            )
            return JsonResponse({'message': 'Cartão aprovado'})
        else:
            return JsonResponse({'message': 'Sua solicitação de crédito foi negado pois seu saldo é insuficiente.'})

            
    
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
            
            if type_transaction in ["PIX", "TRANSFERENCIA"]:
                if conta_sender.saldo < valor:
                    return JsonResponse({'error': "Saldo insuficiente para realizar a transação"}, status=400)
                elif conta_sender.saldo == 0:
                    return JsonResponse({'message': 'Você não tem saldo suficiente para realizar essa transação'})
                else:
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
                deposito = Transaction.objects.create(
                    id_cliente = conta_sender,
                    valor = valor,
                    transaction_type = type_transaction,
                    conta_receiver = conta_sender
                )
                
                deposito.conta_receiver.saldo += valor
                deposito.conta_receiver.save()
                
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

        
class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    
    def create(self, request):
        try:
            loan = request.data
            cliente = loan['id_cliente']
            valor_solicitado = Decimal(loan['valor_solicitado'])
            conta_cliente = AccountCustomer.objects.filter(id=cliente).first()
            salario = float(loan['salario'])
            parcelas = loan['parcelas']
            
            if parcelas <= 24:
                if salario >= 1800.00:
                    Loan.objects.create(
                        id_cliente=conta_cliente,
                        valor_solicitado=valor_solicitado,
                        salario=salario,
                        parcelas=parcelas,
                        aprovado=True
                    ) 
                    
                    conta_cliente.saldo += valor_solicitado
                    conta_cliente.save()
                                
                    return JsonResponse({'message': 'Emprestimo concedido com sucesso.'})
                else:
                    return JsonResponse({'message': 'Seu emprestimo foi negado'})
                
            else:
                return JsonResponse({'message': 'O numero permitido de parcelas deve ser de até 24'})
        except:
            return JsonResponse({'message': 'Não foi possível fazer o emprestimo'})
        
        