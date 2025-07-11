# Generated by Django 5.2.1 on 2025-06-17 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0017_remove_carro_carro_obs'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car_inventory',
            options={'ordering': ['-car_date'], 'verbose_name': 'Inventário'},
        ),
        migrations.AlterModelOptions(
            name='carro',
            options={'verbose_name_plural': 'Carros'},
        ),
        migrations.AddField(
            model_name='carro',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]
