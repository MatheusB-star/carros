# Generated by Django 5.0.7 on 2025-03-12 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0002_categoria_subcategoria_produto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategoria',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='sub_categoria',
        ),
        migrations.DeleteModel(
            name='categoria',
        ),
        migrations.DeleteModel(
            name='produto',
        ),
        migrations.DeleteModel(
            name='subcategoria',
        ),
    ]
