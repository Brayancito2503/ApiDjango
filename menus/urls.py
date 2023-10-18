from django.urls import path, include
from rest_framework import routers
from .views import MenuView, MenuRolView

routers = routers.DefaultRouter()

routers.register(r'', MenuView, 'menus')

routers.register(r'', MenuRolView, 'menurol')


urlpatterns = [
    path("", include(routers.urls))
]