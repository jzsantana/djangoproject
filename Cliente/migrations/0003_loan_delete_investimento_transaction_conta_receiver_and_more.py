# Generated by Django 4.2.7 on 2023-11-24 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente', '0002_rename_movimentacao_transaction_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_solicitado', models.DecimalField(decimal_places=2, max_digits=10)),
                ('parcelas', models.IntegerField(default=0)),
                ('id_cliente_conta', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='Cliente.accountcustomer')),
            ],
        ),
        migrations.DeleteModel(
            name='Investimento',
        ),
        migrations.AddField(
            model_name='transaction',
            name='conta_receiver',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(choices=[('PIX', 'PIX'), ('TRANSFERENCIA', 'Transferência'), ('DEPOSITO', 'Depósito'), ('DEBITO', 'Débito')], default=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='valor',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]