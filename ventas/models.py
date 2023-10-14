from django.db import models
from login.models import Personal
from compras_inventario.models import Productos

# Create your models here.

class Venta(models.Model):
    idventa = models.AutoField(primary_key=True)
    idcliente = models.ForeignKey('Clientes', models.DO_NOTHING, db_column='idcliente', blank=True, null=True)
    cantidad = models.DecimalField(max_digits=2, decimal_places=2, blank=True, null=True)
    precioventa = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    esactivo = models.BooleanField(blank=True, null=True)
    fechaventa = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'venta'


class Clientes(models.Model):
    idcliente = models.AutoField(primary_key=True)
    idpersonal = models.ForeignKey(Personal, models.DO_NOTHING, db_column='idpersonal', blank=True, null=True)
    nombrecompleto = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'clientes'

class Detalleventa(models.Model):
    iddetventa = models.AutoField(primary_key=True)
    idproducto = models.ForeignKey(Productos, models.DO_NOTHING, db_column='idproducto', blank=True, null=True)
    idventa = models.ForeignKey('Venta', models.DO_NOTHING, db_column='idventa', blank=True, null=True)
    cantidad = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    precio = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    fechaventa = models.DateTimeField(blank=True, null=True)
    esactivo = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'detalleventa'

class Mesas(models.Model):
    idmesa = models.AutoField(primary_key=True)
    idcliente = models.ForeignKey('Clientes', models.DO_NOTHING, db_column='idcliente', blank=True, null=True)
    idpersonal = models.ForeignKey(Personal, models.DO_NOTHING, db_column='idpersonal', blank=True, null=True)
    numeromesa = models.IntegerField(blank=True, null=True)
    esactivo = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'mesas'