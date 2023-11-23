# Generated by Django 4.2.7 on 2023-11-23 13:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente', '0007_customer_is_superuser'),
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
                ('id_cliente', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
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
        migrations.RemoveField(
            model_name='cartaodebito',
            name='id_cliente_conta',
        ),
        migrations.RemoveField(
            model_name='clienteconta',
            name='id_cliente',
        ),
        migrations.DeleteModel(
            name='CartaoCredito',
        ),
        migrations.DeleteModel(
            name='CartaoDebito',
        ),
        migrations.AlterField(
            model_name='movimentacao',
            name='id_cliente_conta',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='Cliente.accountcustomer'),
        ),
        migrations.DeleteModel(
            name='ClienteConta',
        ),
    ]
