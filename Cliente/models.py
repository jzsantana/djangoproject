from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
# from .views import SorteioUnico
import random


class SorteioUnico:
    def __init__(self, inicio, fim):
        self.range = set(range(inicio, fim + 1))

    def sortear_numero(self):
        if not self.range:
            raise ValueError
        
        numero_sorteado = random.choice(list(self.range))
        self.range.remove(numero_sorteado)
        return numero_sorteado


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
    telefone = models.CharField(max_length=11)
    cep = models.CharField(max_length=8, default="")
    cidade = models.CharField(max_length=80, default="")
    uf = models.CharField(max_length=2, default="")
    endereco = models.CharField(max_length=255, default="")
    bairro = models.CharField(max_length=80, default="")
    num_casa = models.CharField(max_length=6, default=None)
    senha = models.CharField(max_length=8)
    
    # a pi tem que retornar um amensgame caso o cliente faça uma transferencia 
    # com valor acima do que há na conta
    
    def __str__(self):
        return self.nome


class ClienteConta(models.Model):
    id_cliente = models.ForeignKey(Cliente, editable=False, on_delete=models.CASCADE)
    num_conta = models.IntegerField()
    agencia = models.CharField(max_length=4, default='0001')
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.num_conta


class CartaoDebito(models.Model):
    num_cartao_debito = models.CharField(max_length=16)
    id_cliente_conta = models.ForeignKey(ClienteConta, editable=False, on_delete=models.CASCADE)
    ativo = models.BooleanField()
    senha_debito = models.IntegerField()
    cvv_debito = models.IntegerField()
    # vencimento??
    # nome impresso no cartao??
    
    def __str__(self):
        return self.num_cartao_debito


class CartaoCredito(models.Model):
    num_cartao_credito = models.CharField(max_length=16, default=True)
    id_cliente_conta = models.ForeignKey(ClienteConta, editable=False, on_delete=models.CASCADE)
    ativo = models.BooleanField()
    senha_credito = models.CharField(max_length=6, default=True)
    limite = models.DecimalField(max_digits=10, decimal_places=2)
    cvv_credito = models.IntegerField(default=True)
    
    def __str__(self):
        return self.num_cartao_credito


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
    

@receiver(post_save, sender=Cliente)
def criar_conta(sender, instance, created, **kwargs):
    if created:
        sorteio = SorteioUnico(100000, 999999)
        num_conta = sorteio.sortear_numero()
        
        ClienteConta.objects.create(
            id_cliente=instance,
            agencia = '0001',
            num_conta = num_conta,
            saldo = 0.0
        )
        
        
@receiver(post_save, sender=ClienteConta)
def criar_carta_debito(sender, instance, created, **kwargs):
    if created:
        sorteio_senha_cartao = SorteioUnico(1000, 9999)
        sorteio_cvv = SorteioUnico(100, 999)
        
        num_cartao_debito = 1231586478946658
        ativo = True
        senha_debito = sorteio_senha_cartao.sortear_numero()
        cvv_debito = sorteio_cvv.sortear_numero()
        
        CartaoDebito.objects.create(
            id_cliente_conta = instance,
            num_cartao_debito = num_cartao_debito,
            ativo = ativo,
            senha_debito = senha_debito,
            cvv_debito = cvv_debito
        )
    

