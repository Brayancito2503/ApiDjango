from django.db import models

# Create your models here.
class Compras(models.Model):
    idcompra = models.AutoField(primary_key=True)
    idproveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='idproveedor', blank=True, null=True)
    idcatcompra = models.ForeignKey('Categoriacompra', models.DO_NOTHING, db_column='idcatcompra', blank=True, null=True)
    nombrecompra = models.TextField(blank=True, null=True)
    total = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    tipopago = models.BooleanField(blank=True, null=True)
    fechacompra = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'compras'

class Proveedor(models.Model):
    idproveedor = models.AutoField(primary_key=True)
    ruc = models.TextField(blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    nombreproveedor = models.CharField(max_length=20, blank=True, null=True)
    fecharegistro = models.DateTimeField(blank=True, null=True)
    empresa = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'proveedor'




class Categoriacompra(models.Model):
    idcatcompra = models.AutoField(primary_key=True)
    nombrecategoria = models.CharField(max_length=20, blank=True, null=True)
    fecharegistro = models.DateTimeField(blank=True, null=True)
    esactivo = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'categoriacompra'



class Productos(models.Model):
    idproducto = models.AutoField(primary_key=True)
    idcatproducto = models.ForeignKey('Categoriaproducto', models.DO_NOTHING, db_column='idcatproducto', blank=True, null=True)
    nombreproducto = models.TextField(blank=True, null=True)
    preciocompra = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    precioventa = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    fecharegistro = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'productos'


class Categoriaproducto(models.Model):
    idcatproducto = models.AutoField(primary_key=True)
    nombrecatproducto = models.CharField(max_length=30, blank=True, null=True)
    fecharegistro = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'categoriaproducto'


class Detallecompra(models.Model):
    iddetcompra = models.AutoField(primary_key=True)
    idcompra = models.ForeignKey('Compras', models.DO_NOTHING, db_column='idcompra', blank=True, null=True)
    idproducto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='idproducto', blank=True, null=True)
    cantidad = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    precio = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    fechadetcompra = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'detallecompra'

