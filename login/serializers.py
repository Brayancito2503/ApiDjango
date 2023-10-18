from rest_framework import serializers
from .models import Personal, Rol

class PersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal
        #fields = ('idpersonal', 'idrol', 'nombre', 'apellido', 'telefono','correo','clave','esactivo','fecharegistro')
        fields = '__all__'

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        #fields = ('idrol','nombrerol','esactivo','fecharegistro')
        fields = '__all__'
