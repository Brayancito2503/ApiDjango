
from django.urls import path, include
from rest_framework import routers
from .views import RolView

#va a tomar las vistas y va a generar las urls
routers = routers.DefaultRouter()
#registrar un nueva vista
routers.register(r'roles', RolView, 'roles')

#versionado de la api
urlpatterns = [
    path("api/v1/", include(routers.urls) )

]
