# Generated by Django 4.2.5 on 2023-09-26 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_rename_usuario_usuarios'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='icono',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='usuarios',
            name='nombreMenu',
            field=models.CharField(default='DashBorad', max_length=30),
            preserve_default=False,
        ),
    ]
