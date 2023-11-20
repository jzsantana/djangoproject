from rest_framework import viewsets
# from rest_framework import serializers
from Cliente.models import Cliente, CartaoCredito, CartaoDebito, ClienteConta
from rest_framework import filters
from Cliente.serializers import ClienteSerializer, CartaoDebitoSerializer, ClienteContaSerializer
# # from django_filters.rest_framework import DjangoFilterBackend


class ClienteViewSet(viewsets.ModelViewSet):
    queryset =  Cliente.objects.all()
    serializer_class = ClienteSerializer
    

class ContaClienteViewSet(viewsets.ModelViewSet):
    queryset = ClienteConta.objects.all()
    serializer_class = ClienteContaSerializer
    

class CartaoDebitoViewSet(viewsets.ModelViewSet):
    queryset = CartaoDebito.objects.all()
    serializer_class = CartaoDebitoSerializer
    
    