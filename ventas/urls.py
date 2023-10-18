from django.urls import path, include
from rest_framework import routers
from .views import ClientesView, DetalleVentaView, MesasView, VentaView

routers = routers.DefaultRouter()

routers.register(r'',ClientesView, 'Clientes')
routers.register(r'',DetalleVentaView, 'DetalleVenta')
routers.register(r'', MesasView, 'Mesas')
routers.register(r'', VentaView, 'Ventas')  

urlpatterns = [
    path("", include(routers.urls))
]