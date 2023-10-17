from rest_framework import viewsets
from .serializers import RolSerializer
from .models import Rol
# Create your views here.

class RolView(viewsets.ModelViewSet):
    serializer_class = RolSerializer
    queryset = Rol.objects.all()
