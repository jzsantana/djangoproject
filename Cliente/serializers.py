from rest_framework import serializers
from .models import Cliente, ClienteConta, CartaoCredito, CartaoDebito
# from Cliente import models

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        
        
class ClienteContaSerializer(serializers.ModelSerializer):
    id_cliente = ClienteSerializer()


    class Meta:
        model = ClienteConta
        fields = (
            'id_cliente',
            'num_conta',
            'agencia',
            'saldo',
            'data_criacao'
        )
    
        
class CartaoDebitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartaoDebito
        fields = '__all__'
        
        
class CartaoCreditoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartaoCredito
        fields = '__all__'
                
