# Generated by Django 4.2.7 on 2023-11-23 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente', '0004_customer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={},
        ),
        migrations.RemoveField(
            model_name='customer',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='username',
        ),
    ]
