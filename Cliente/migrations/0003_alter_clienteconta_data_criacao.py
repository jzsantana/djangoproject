# Generated by Django 4.2.7 on 2023-11-17 14:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente', '0002_clienteconta_data_criacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clienteconta',
            name='data_criacao',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
