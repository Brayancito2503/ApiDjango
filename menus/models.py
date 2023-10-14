from django.db import models
from login.models import Rol


# Create your models here.
class Menu(models.Model):
    idmenu = models.AutoField(primary_key=True)
    nombremenu = models.CharField(max_length=30, blank=True, null=True)
    icono = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'menu'


class Menurol(models.Model):
    idmenurol = models.AutoField(primary_key=True)
    idmenu = models.ForeignKey('Menu', models.DO_NOTHING, db_column='idmenu', blank=True, null=True)
    idrol = models.ForeignKey(Rol, models.DO_NOTHING, db_column='idrol', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'menurol'
