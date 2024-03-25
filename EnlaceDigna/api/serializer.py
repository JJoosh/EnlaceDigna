from rest_framework import serializers
from ..models import Ultrasonidos  # Ajusta este importe según la estructura de tu proyecto
from ..models import Usuarios
from ..models import Doctores
class UltrasonidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ultrasonidos
        fields = ['id', 'ruta_files', 'id_usuario', 'tipo_ultrasonido', 'fecha']


class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model=Usuarios
        fields='__all__'

class DoctoresSerializer(serializers.ModelSerializer):
    class Meta:
        model=Doctores
        fields='__all__'

