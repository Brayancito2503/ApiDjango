from rest_framework import serializers
from .models import Menu, Menurol

class MenuSerializers(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class MenuRolSerializers(serializers.ModelSerializer):
    class Meta:
        model = Menurol
        fields = '__all__'