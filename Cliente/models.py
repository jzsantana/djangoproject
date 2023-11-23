from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from datetime import datetime
import random

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class SorteioUnico:
    def __init__(self, inicio, fim):
        self.range = list(range(inicio, fim + 1))

    def sortear_numero(self):
        if not self.range:
            raise ValueError
        
        numero_sorteado = random.choice(list(self.range))
        self.range.remove(numero_sorteado)
        return numero_sorteado


class ManagerUser(BaseUserManager):
    # isso significa que ele realmente vai estar no bd, ou seja, ele vai ser uma tabela no bd
    use_in_migrations = True
    
    # responsavel por salvar tanto o usuario comum quanto o usuario admin
    def _create_user(self, email, cpf, password, **extra_fields):
        if not email:
            raise ValueError('The account number is mandatory')
        email = self.normalize_email(email)
        user = self.model(email=email, cpf=cpf, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    
    def create_user(self, email, cpf,password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, cpf,password, **extra_fields)
    
    
    def create_superuser(self, email, cpf, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('SuperUser precisa ter is_superuser')
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('SuperUser precisa ter is_staff')
        
        return self._create_user(email, cpf, password, **extra_fields)
        
    
# CustomUser
class Customer(AbstractBaseUser):
    
    PJ = "PESSOA JURIDICA"
    PF = "PESSOA FISICA"
    
    ACCOUNT_TYPE_CHOICES = [
        ('PF', PF),
        ('PJ', PJ),
    ]
    
    email = models.CharField('E-mail', max_length=180)
    name = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11, unique=True)
    date_birth = models.DateField()
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPE_CHOICES)
    telephone = models.CharField(max_length=11)
    cep = models.CharField(max_length=8)
    city = models.CharField(max_length=80)
    uf = models.CharField(max_length=2)
    address = models.CharField(max_length=255)
    neighborhood = models.CharField(max_length=80)
    house_num = models.CharField(max_length=6)
    # password = models.CharField(max_length=8)
    is_staff = models.BooleanField(default=True) 
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'cpf'
    REQUIRED_FIELDS = [
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
        'house_num'
    ]
    
    def __str__(self):
        return self.cpf
    
    objects = ManagerUser()
    
    def has_module_perms(self, app_label):
        return True
    
    def has_perm(self, perm, obj=None):
        return self.is_superuser


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


class AccountCustomer(models.Model):
    id_cliente = models.ForeignKey(Customer, editable=False, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=6)
    agency = models.CharField(max_length=4, default='0001')
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    creation_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.account_number


class DebitCard(models.Model):
    debit_card_number = models.CharField(max_length=16)
    id_cliente_conta = models.ForeignKey(AccountCustomer, editable=False, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    debit_password = models.CharField(max_length=4)
    debit_cvv = models.CharField(max_length=3)
    # vencimento??
    # nome impresso no cartao??
    
    def __str__(self):
        return self.num_cartao_debito


class CreditCard(models.Model):
    credit_card_number = models.CharField(max_length=16, default=True)
    id_cliente_conta = models.ForeignKey(AccountCustomer, editable=False, on_delete=models.CASCADE)
    active = models.BooleanField()
    credit_password = models.CharField(max_length=6, default=True)
    limite = models.DecimalField(max_digits=10, decimal_places=2)
    credit_cvv = models.CharField(max_length=3)
    
    
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
    
    id_cliente_conta = models.ForeignKey(AccountCustomer, editable=False, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_movimentacao = models.CharField(max_length=20, choices=MOVIMENTACAO_CHOICES, default=True)
    
    
class Investimento(models.Model):
    
    ...
    

@receiver(post_save, sender=Customer)
def create_account(sender, instance, created, **kwargs):
    if created:
        sorteio = SorteioUnico(100000, 999999)
        num_conta = sorteio.sortear_numero()
        
        AccountCustomer.objects.create(
            id_cliente=instance,
            account_number = num_conta,
        )
        
        
@receiver(post_save, sender=AccountCustomer)
def criar_cartao_debito(sender, instance, created, **kwargs):
    if created:
        sorteio_senha_cartao = SorteioUnico(1000, 9999)
        sorteio_cvv = SorteioUnico(100, 999)
        num_cartao_debito= str(random.randint(1000000000000000, 9999999999999998))
    
        senha_debito = sorteio_senha_cartao.sortear_numero()
        cvv_debito = sorteio_cvv.sortear_numero()
        
        DebitCard.objects.create(
            id_cliente_conta = instance,
            debit_card_number = num_cartao_debito,
            debit_password = senha_debito,
            debit_cvv = cvv_debito
        )
    

