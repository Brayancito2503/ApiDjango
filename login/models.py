from django.db import models

# Create your models here.
class Personal(models.Model):
    idpersonal = models.AutoField(primary_key=True)
    idrol = models.ForeignKey('Rol', models.DO_NOTHING, db_column='idrol', blank=True, null=True)
    nombre = models.CharField(max_length=30, blank=True, null=True)
    apellido = models.CharField(max_length=30, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    correo = models.TextField(blank=True, null=True)
    clave = models.TextField(blank=True, null=True)
    esactivo = models.BooleanField(blank=True, null=True)
    fecharegistro = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'personal'

class Rol(models.Model):
    idrol = models.AutoField(primary_key=True)
    nombrerol = models.CharField(max_length=25, blank=True, null=True)
    esactivo = models.BooleanField(blank=True, null=True)
    fecharegistro = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'rol'