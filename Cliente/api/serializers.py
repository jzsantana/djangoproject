from rest_framework import serializers
import models

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
        