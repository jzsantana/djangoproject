from django.db import models

# Create your models here.
class Cliente(models.Model):
    PJ = "PESSOA JURIDICA"
    PF = "PESSOA FISICA"
    
    TIPO_CONTA_CHOICES = [
        ('PF', PF),
        ('PJ', PJ),
    ]
    
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    tipo_conta = models.CharField(max_length=20, choices=TIPO_CONTA_CHOICES)
    cep = models.CharField(max_length=8, default="")
    cidade = models.CharField(max_length=80, default="")
    uf = models.CharField(max_length=2, default="")
    endereco = models.CharField(max_length=255, default="")
    bairro = models.CharField(max_length=80, default="")
    num_casa = models.CharField(max_length=6, default=None)
    
    def __str__(self):
        return self.nome


class ClienteConta(models.Model):
    id_cliente = models.ForeignKey(Cliente, editable=False, on_delete=models.CASCADE, default="")
    num_conta = models.IntegerField()
    agencia = models.CharField(max_length=4)
    senha = models.CharField(max_length=8)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.num_conta


class CartaoDebito(models.Model):
    num_cartao_debito = models.CharField(max_length=16)
    id_cliente_conta = models.ForeignKey(ClienteConta, editable=False, on_delete=models.CASCADE)
    ativo = models.BooleanField()
    senha_debito = models.CharField(max_length=4)
    cvv_debito = models.IntegerField()


class CartaoCredito(models.Model):
    num_cartao_credito = models.CharField(max_length=16, default=True)
    id_cliente_conta = models.ForeignKey(ClienteConta, editable=False, on_delete=models.CASCADE)
    ativo = models.BooleanField()
    senha_credito = models.CharField(max_length=6, default=True)
    limite = models.DecimalField(max_digits=10, decimal_places=2)
    cvv_credito = models.IntegerField(default=True)


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
    
