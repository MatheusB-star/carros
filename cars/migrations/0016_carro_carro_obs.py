# Generated by Django 5.2.1 on 2025-06-04 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0015_car_inventory'),
    ]

    operations = [
        migrations.AddField(
            model_name='carro',
            name='carro_obs',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
