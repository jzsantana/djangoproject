from rest_framework import serializers
# from .models import Cliente, CartaoCredito, CartaoDebito
from .models import AccountCustomer, DebitCard, CreditCard, Customer
from datetime import datetime
# from Cliente import models


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = [ 
                'id',
                'email',
                'account_type',
                'name',
                'date_birth',
                'telephone',
                'cep',
                'city',
                'uf',
                'address',
                'neighborhood',
                'house_num',
                'cpf'
                ]
        

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
                
