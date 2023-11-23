from rest_framework import viewsets
# from rest_framework import serializers
# from Cliente.models import Cliente, CartaoDebito
from rest_framework import filters
from Cliente.serializers import CustomerSerializer, DebitCardSerializer, AccountCustomerSerializer
# # from django_filters.rest_framework import DjangoFilterBackend
from Cliente.models import Customer, AccountCustomer, DebitCard, CreditCard


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    

# class ClienteViewSet(viewsets.ModelViewSet):
#     queryset =  Cliente.objects.all()
#     serializer_class = ClienteSerializer
    

class AccountCustomerViewSet(viewsets.ModelViewSet):
    queryset = AccountCustomer.objects.all()
    serializer_class = AccountCustomerSerializer
    

class DebitCardViewSet(viewsets.ModelViewSet):
    queryset = DebitCard.objects.all()
    serializer_class = DebitCardSerializer
    
    