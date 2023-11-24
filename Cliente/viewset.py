from rest_framework import viewsets
# from rest_framework import serializers
# from Cliente.models import Cliente, CartaoDebito
from rest_framework import filters
from Cliente.serializers import DebitCardSerializer, AccountCustomerSerializer
# # from django_filters.rest_framework import DjangoFilterBackend
from Cliente.models import  AccountCustomer, DebitCard


# class CustomerViewSet(viewsets.ModelViewSet):
    # queryset = Customer.objects.all()
    # serializer_class = CustomerSerializer
    

class AccountCustomerViewSet(viewsets.ModelViewSet):
    queryset = AccountCustomer.objects.all()
    serializer_class = AccountCustomerSerializer
    

class DebitCardViewSet(viewsets.ModelViewSet):
    queryset = DebitCard.objects.all()
    serializer_class = DebitCardSerializer
    
    