from rest_framework import viewsets
from .serializers import MenuSerializers, MenuRolSerializers
from .models import Menu, Menurol 

# Create your views here.

class MenuView(viewsets.ModelViewSet):
    # Establece el serializador que se utilizará para convertir objetos del modelo en datos JSON y viceversa.
    serializer_class = MenuSerializers

    # Define la consulta (queryset) que se utilizará para obtener los objetos del modelo "Rol."
    queryset = Menu.objects.all()

class MenuRolView(viewsets.ModelViewSet):
    serializer_class = MenuRolSerializers
    queryset = Menurol.objects.all()