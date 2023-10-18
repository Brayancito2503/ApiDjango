from rest_framework import viewsets
from .serializers import ClientesSerializers, DetalleventaSerializers, MesasSerializers, VentaSerializers
from .models import Clientes, Detalleventa, Mesas, Venta

# Create your views here.

class ClientesView(viewsets.ModelViewSet):
    serializer_class = ClientesSerializers
    queryset = Clientes.objects.all()

class DetalleVentaView(viewsets.ModelViewSet):
    serializer_class = DetalleventaSerializers
    queryset = Detalleventa.objects.all()

class MesasView(viewsets.ModelViewSet):
    serializer_class = MesasSerializers
    queryset = Mesas.objects.all()

class VentaView(viewsets.ModelViewSet):
    serializer_class = VentaSerializers
    queryset = Venta.objects.all()