# Generated by Django 5.0.7 on 2025-01-27 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0013_alter_usuario_usuario_quando'),
    ]

    operations = [
        migrations.DeleteModel(
            name='usuario',
        ),
    ]
