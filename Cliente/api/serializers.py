from rest_framework import serializers
# from .models import Cliente, ClienteConta, CartaoCredito, CartaoDebito
from Cliente import models

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cliente
        fields = '__all__'
        
        
class ClienteContaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ClienteConta
        fields = '__all__'
        
        
class CartaoDebitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CartaoDebito
        fields = '__all__'
        
        
class CartaoCreditoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CartaoCredito
        fields = '__all__'
                
