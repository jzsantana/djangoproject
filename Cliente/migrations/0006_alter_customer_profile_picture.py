# Generated by Django 4.2.7 on 2023-12-11 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente', '0005_alter_customer_profile_picture_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to='perfil/'),
        ),
    ]
