# Generated by Django 4.2.5 on 2023-10-04 00:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppEduca', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entrega_de_proyecto',
            old_name='entregada',
            new_name='entrega',
        ),
    ]
