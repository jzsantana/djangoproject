from rest_framework import serializers
# from .models import Cliente, CartaoCredito, CartaoDebito
from .models import Customer, AccountCustomer, DebitCard, CreditCard
# from Cliente import models


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        

# class ClienteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Cliente
#         fields = '__all__'
        
        
class AccountCustomerSerializer(serializers.ModelSerializer):
    id_cliente = CustomerSerializer()


    class Meta:
        model = AccountCustomer
        fields = (
            'id_cliente',
            'account_number',
            'agency',
            'saldo',
            'creation_date'
        )
    
        
class DebitCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = DebitCard
        fields = '__all__'
        
        
class CreditCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditCard
        fields = '__all__'
                
