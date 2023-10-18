
from django.urls import path, include
from rest_framework import routers
from .views import RolView, PersonalView

# las funciones path e include de Django para definir rutas URL y para incluir las rutas del enrutador en el archivo de URL principal.
# el módulo routers de Django REST framework que proporciona un enrutador que simplifica la definición de rutas URL para las vistas basadas en clases.

# Crea una instancia de un enrutador predeterminado proporcionado por Django REST framework. 
# Este enrutador simplifica la creación de rutas URL basadas en las vistas que registres.
#va a tomar las vistas y va a generar las urls
routers = routers.DefaultRouter()

# registrar un nueva vista
# Registra la vista RolView en el enrutador con el nombre "roles." 
routers.register(r'roles', RolView, 'roles')

# Registra la vista "PersonalView" en el enrutador para "personal."
routers.register(r'personal', PersonalView, 'personal')

#versionado de la api
urlpatterns = [
    path("api/v1/", include(routers.urls))
]
