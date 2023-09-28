# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Categoriacompra(models.Model):
    idcatcompra = models.AutoField(primary_key=True)
    nombrecategoria = models.CharField(max_length=20, blank=True, null=True)
    fecharegistro = models.DateTimeField(blank=True, null=True)
    esactivo = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categoriacompra'


class Categoriaproducto(models.Model):
    idcatproducto = models.AutoField(primary_key=True)
    nombrecatproducto = models.CharField(max_length=30, blank=True, null=True)
    fecharegistro = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categoriaproducto'


class Clientes(models.Model):
    idcliente = models.AutoField(primary_key=True)
    idpersonal = models.ForeignKey('Personal', models.DO_NOTHING, db_column='idpersonal', blank=True, null=True)
    nombrecompleto = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clientes'


class Compras(models.Model):
    idcompra = models.AutoField(primary_key=True)
    idproveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='idproveedor', blank=True, null=True)
    idcatcompra = models.ForeignKey(Categoriacompra, models.DO_NOTHING, db_column='idcatcompra', blank=True, null=True)
    nombrecompra = models.TextField(blank=True, null=True)
    total = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    tipopago = models.BooleanField(blank=True, null=True)
    fechacompra = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compras'


class Detallecompra(models.Model):
    iddetcompra = models.AutoField(primary_key=True)
    idcompra = models.ForeignKey(Compras, models.DO_NOTHING, db_column='idcompra', blank=True, null=True)
    idproducto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='idproducto', blank=True, null=True)
    cantidad = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    precio = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    fechadetcompra = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detallecompra'


class Detalleventa(models.Model):
    iddetventa = models.AutoField(primary_key=True)
    idproducto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='idproducto', blank=True, null=True)
    idventa = models.ForeignKey('Venta', models.DO_NOTHING, db_column='idventa', blank=True, null=True)
    cantidad = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    precio = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    fechaventa = models.DateTimeField(blank=True, null=True)
    esactivo = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalleventa'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Menu(models.Model):
    idmenu = models.AutoField(primary_key=True)
    nombremenu = models.CharField(max_length=30, blank=True, null=True)
    icono = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu'


class Menurol(models.Model):
    idmenurol = models.AutoField(primary_key=True)
    idmenu = models.ForeignKey(Menu, models.DO_NOTHING, db_column='idmenu', blank=True, null=True)
    idrol = models.ForeignKey('Rol', models.DO_NOTHING, db_column='idrol', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menurol'


class Mesas(models.Model):
    idmesa = models.AutoField(primary_key=True)
    idcliente = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='idcliente', blank=True, null=True)
    idpersonal = models.ForeignKey('Personal', models.DO_NOTHING, db_column='idpersonal', blank=True, null=True)
    numeromesa = models.IntegerField(blank=True, null=True)
    esactivo = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mesas'


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
        managed = False
        db_table = 'personal'


class Productos(models.Model):
    idproducto = models.AutoField(primary_key=True)
    idcatproducto = models.ForeignKey(Categoriaproducto, models.DO_NOTHING, db_column='idcatproducto', blank=True, null=True)
    nombreproducto = models.TextField(blank=True, null=True)
    preciocompra = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    precioventa = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    fecharegistro = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productos'


class Proveedor(models.Model):
    idproveedor = models.AutoField(primary_key=True)
    ruc = models.TextField(blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    nombreproveedor = models.CharField(max_length=20, blank=True, null=True)
    fecharegistro = models.DateTimeField(blank=True, null=True)
    empresa = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proveedor'


class Rol(models.Model):
    idrol = models.AutoField(primary_key=True)
    nombrerol = models.CharField(max_length=25, blank=True, null=True)
    esactivo = models.BooleanField(blank=True, null=True)
    fecharegistro = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rol'


class Venta(models.Model):
    idventa = models.AutoField(primary_key=True)
    idcliente = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='idcliente', blank=True, null=True)
    cantidad = models.DecimalField(max_digits=2, decimal_places=2, blank=True, null=True)
    precioventa = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    esactivo = models.BooleanField(blank=True, null=True)
    fechaventa = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'venta'
