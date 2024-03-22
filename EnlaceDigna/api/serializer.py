from rest_framework import serializers
from ..models import Ultrasonidos  # Ajusta este importe según la estructura de tu proyecto

class UltrasonidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ultrasonidos
        fields = ['id', 'ruta_files', 'usuario', 'tipo_ultrasonido', 'fecha']
