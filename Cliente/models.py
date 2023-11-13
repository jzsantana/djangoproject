from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    tipo_conta = models.CharField(max_length=20)
    cep = models.CharField(max_length=8)


class ClienteConta(models.Model):
    num_conta = models.IntegerField()
    agencia = models.CharField(max_length=3)
    senha = models.CharField(max_length=8)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)


class CartaoDebito(models.Model):
    num_cartao_debito = models.IntegerField()
    id_cliente_conta = models.ForeignKey(ClienteConta, editable=False, on_delete=models.CASCADE)
    ativo = models.BooleanField()
    cvv = models.IntegerField()


class CartaoCredito(models.Model):
    num_cartao_credito = models.IntegerField()
    id_cliente_conta = models.ForeignKey(ClienteConta, editable=False, on_delete=models.CASCADE)
    ativo = models.BooleanField()
    limite = models.DecimalField(max_digits=10, decimal_places=2)
    cvv = models.IntegerField()


class Movimentacao(models.Model):
    
    PIX = "PIX"
    TRANSFERENCIA = "Transferência"
    DEPOSITO = "Depósito"
    
    MOVIMENTACAO_CHOICES = [
        ('PIX', PIX),
        ('TRANSFERENCIA', TRANSFERENCIA),
        ('DEPOSITO', DEPOSITO)
    ]
    
    id_cliente_conta = models.ForeignKey(ClienteConta, editable=False, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_movimentacao = models.CharField(max_length=20, choices=MOVIMENTACAO_CHOICES, default=True)
    
    
class Investimento(models.Model):
    
    ...
    
