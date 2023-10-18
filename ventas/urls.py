from django.urls import path, include
from rest_framework import routers
from .views import ClientesView, DetalleVentaView, MesasView, VentaView

routers = routers.DefaultRouter()

routers.register(r'clientes',ClientesView, 'Clientes')
routers.register(r'detalleventa',DetalleVentaView, 'DetalleVenta')
routers.register(r'mesas', MesasView, 'Mesas')
routers.register(r'ventas', VentaView, 'Ventas')  

urlpatterns = [
    path("", include(routers.urls))
]