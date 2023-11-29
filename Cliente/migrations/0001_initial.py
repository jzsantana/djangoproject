# Generated by Django 4.2.7 on 2023-11-24 12:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountCustomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.CharField(max_length=6)),
                ('agency', models.CharField(default='0001', max_length=4)),
                ('saldo', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('creation_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Investimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.CharField(max_length=180, verbose_name='E-mail')),
                ('name', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('date_birth', models.DateField()),
                ('account_type', models.CharField(choices=[('PF', 'PESSOA FISICA'), ('PJ', 'PESSOA JURIDICA')], max_length=20)),
                ('telephone', models.CharField(max_length=11)),
                ('cep', models.CharField(max_length=8)),
                ('city', models.CharField(max_length=80)),
                ('uf', models.CharField(max_length=2)),
                ('address', models.CharField(max_length=255)),
                ('neighborhood', models.CharField(max_length=80)),
                ('house_num', models.CharField(max_length=6)),
                ('is_staff', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
            },
        ),
        migrations.CreateModel(
            name='Movimentacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tipo_movimentacao', models.CharField(choices=[('PIX', 'PIX'), ('TRANSFERENCIA', 'Transferência'), ('DEPOSITO', 'Depósito')], default=True, max_length=20)),
                ('id_cliente_conta', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='Cliente.accountcustomer')),
            ],
        ),
        migrations.CreateModel(
            name='DebitCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debit_card_number', models.CharField(max_length=16)),
                ('active', models.BooleanField(default=True)),
                ('debit_password', models.CharField(max_length=4)),
                ('debit_cvv', models.CharField(max_length=3)),
                ('id_cliente_conta', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='Cliente.accountcustomer')),
            ],
        ),
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit_card_number', models.CharField(default=True, max_length=16)),
                ('active', models.BooleanField()),
                ('credit_password', models.CharField(default=True, max_length=6)),
                ('limite', models.DecimalField(decimal_places=2, max_digits=10)),
                ('credit_cvv', models.CharField(max_length=3)),
                ('id_cliente_conta', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='Cliente.accountcustomer')),
            ],
        ),
        migrations.AddField(
            model_name='accountcustomer',
            name='id_cliente',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
