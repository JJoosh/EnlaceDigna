from rest_framework import serializers
from .models import Usuarios
class usuarios_seriazer(serializers.ModelSerializer):
    class Meta:
        model=Usuarios
        fields='__all__'
        