# Generated by Django 5.0.7 on 2024-08-08 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_carro_carro_obs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carro',
            name='placa',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
