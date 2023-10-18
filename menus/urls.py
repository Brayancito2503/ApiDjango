from django.urls import path, include
from rest_framework import routers
from .views import MenuView, MenuRolView

routers = routers.DefaultRouter()

routers.register(r'menu', MenuView, 'menus')

routers.register(r'menurol', MenuRolView, 'menurol')


urlpatterns = [
    path("", include(routers.urls))
]