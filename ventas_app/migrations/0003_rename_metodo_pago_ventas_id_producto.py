# Generated by Django 5.1 on 2024-11-28 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas_app', '0002_ventas_estatus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ventas',
            old_name='metodo_pago',
            new_name='id_producto',
        ),
    ]