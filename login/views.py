from rest_framework import viewsets
from .serializers import RolSerializer, PersonalSerializer
from .models import Rol, Personal
# Create your views here.

class RolView(viewsets.ModelViewSet):
    # Establece el serializador que se utilizará para convertir objetos del modelo en datos JSON y viceversa.
    serializer_class = RolSerializer

    # Define la consulta (queryset) que se utilizará para obtener los objetos del modelo "Rol."
    queryset = Rol.objects.all()

class PersonalView(viewsets.ModelViewSet):
    serializer_class = PersonalSerializer
    queryset =  Personal.objects.all()