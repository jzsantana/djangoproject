from rest_framework import serializers
from .models import AccountCustomer, DebitCard, CreditCard, Customer, Transaction


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [ 
                'id',
                'email',
                'cpf',
                'name',
                'account_type',
                'date_birth',
                'telephone',
                'cep',
                'city',
                'uf',
                'address',
                'neighborhood',
                'house_num'
                ]
        

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = (
                    'id',
                    'id_cliente',
                    'valor',
                    'transaction_type',
                    'conta_receiver',
                    'timestamp'
                  )


class AccountCustomerSerializer(serializers.ModelSerializer):

    transaction_sender = TransactionSerializer('id', many=True, read_only=True)

    class Meta:
        model = AccountCustomer
        fields = (
            'id',
            'id_cliente',
            'account_number',
            'agency',
            'saldo',
            'creation_date',
            'transaction_sender'
        )
    
        
class DebitCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = DebitCard
        fields = '__all__'
        
        
class CreditCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditCard
        fields = '__all__'


# class ExtractSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Extract
#         fields = (
#             'id', 
#             'id_cliente',
#             'valor',
#             'conta_receiver'
#         )


