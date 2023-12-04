from django.contrib import admin

from .models import AccountCustomer, DebitCard, CreditCard, Transaction
from .models import Customer

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')


# @admin.register(Cliente)
# class ClienteAdmin(admin.ModelAdmin):
#     list_display = ('id' ,'nome', 'tipo_conta')
#     # ESSE LIST DISPLAY VAI TER OS CAMPOS QUE SERAO EXIBIDOS NA PAGINA DE ADMIN
    
    
@admin.register(AccountCustomer)
class AccountCustomer(admin.ModelAdmin):
    list_display = ('id', 'id_cliente','account_number', 'agency', 'saldo', 'creation_date')
    
    
@admin.register(DebitCard)
class DebitCardAdmin(admin.ModelAdmin):
    list_display = ('debit_card_number', 'active', 'id_cliente_conta')
    
    
@admin.register(CreditCard)
class CreditCardAdmin(admin.ModelAdmin):
    list_display = ('credit_card_number', 'active', 'id_cliente_conta')
    
    
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id_cliente', 'valor', 'transaction_type', 'conta_receiver')


# @admin.register(Extract)
# class ExtractAdmin(admin.ModelAdmin):
#     list_display = ('id_transaction', 'id_cliente')