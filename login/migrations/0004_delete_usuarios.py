# Generated by Django 4.2.5 on 2023-09-27 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_usuarios_icono_usuarios_nombremenu'),
    ]

    operations = [
        migrations.DeleteModel(
            name='usuarios',
        ),
    ]