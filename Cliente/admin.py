from django.contrib import admin

from .models import Cliente, ClienteConta, CartaoDebito, CartaoCredito

# Register your models here.
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo_conta')
    # ESSE LIST DISPLAY VAI TER OS CAMPOS QUE SERAO EXIBIDOS NA PAGINA DE ADMIN
    
    
@admin.register(ClienteConta)
class ClienteContaAdmin(admin.ModelAdmin):
    list_display = ('id_cliente','num_conta', 'agencia', 'saldo', 'data_criacao')
    
    
@admin.register(CartaoDebito)
class CartaoDebitoAdmin(admin.ModelAdmin):
    list_display = ('num_cartao_debito', 'ativo')
    
    
@admin.register(CartaoCredito)
class CartaoCreditoAdmin(admin.ModelAdmin):
    list_display = ('num_cartao_credito', 'ativo')