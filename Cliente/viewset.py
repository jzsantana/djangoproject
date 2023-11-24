from rest_framework import viewsets
from rest_framework import filters
from Cliente.serializers import DebitCardSerializer, AccountCustomerSerializer, CreditCardSerializer, TransactionSerializer
from Cliente.models import  AccountCustomer, DebitCard, CreditCard, Transaction


# class CustomerViewSet(viewsets.ModelViewSet):
    # queryset = Customer.objects.all()
    # serializer_class = CustomerSerializer
    

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
    queryset = Transaction
    serializer_class = TransactionSerializer
    
    