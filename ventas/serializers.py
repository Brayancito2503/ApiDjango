from rest_framework import serializers
from .models import Clientes, Detalleventa, Mesas, Venta 

class ClientesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = '__all__'

class DetalleventaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Detalleventa
        fields = '__all__'

class MesasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mesas
        fields = '__all__'

class VentaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = '__all__'