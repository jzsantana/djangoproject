# Generated by Django 4.2.7 on 2023-11-21 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente', '0002_clienteconta_data_criacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartaocredito',
            name='cvv_credito',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='cartaodebito',
            name='cvv_debito',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='clienteconta',
            name='num_conta',
            field=models.CharField(max_length=6),
        ),
    ]