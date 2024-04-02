import json
from rest_framework import serializers
from ..models import Ultrasonidos  # Ajusta este importe según la estructura de tu proyecto
from rest_framework.fields import ListField
from ..models import Usuarios
from ..models import Doctor
class UltrasonidoSerializer(serializers.ModelSerializer):
    # Agregamos ListField para manejar la lista de URLs en las entradas, no asociado directamente con el modelo
    ruta_files_list = ListField(
        child=serializers.URLField(),
        write_only=True,
        required=False
    )

    class Meta:
        model = Ultrasonidos
        fields = ['id', 'ruta_files', 'TipoDeUltrasonidos', 'Fecha', 'cliente_id', 'ruta_files_list', 'tokenUltrasonido']

    def get_ruta_files(self, obj):
        # Deserializamos la cadena JSON almacenada en la lista para la respuesta
        if obj.ruta_files:
            return json.loads(obj.ruta_files)
        return []

    def create(self, validated_data):
        # Extracción de ruta_files_list y eliminación del campo 'ruta_files_list' ya que no es parte del modelo
        ruta_files_list = validated_data.pop('ruta_files_list', [])
        # Convertimos la lista de URLs a una cadena JSON para almacenarla en la base de datos
        validated_data['ruta_files'] = json.dumps(ruta_files_list)
        return super(UltrasonidoSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        # Si se actualiza el campo 'ruta_files', debe tratarse como una lista y convertirse a JSON
        if 'ruta_files_list' in validated_data:
            ruta_files_list = validated_data.pop('ruta_files_list')
            validated_data['ruta_files'] = json.dumps(ruta_files_list)
        return super(UltrasonidoSerializer, self).update(instance, validated_data)

    def to_representation(self, instance):
        # Convertimos la cadena JSON almacenada en una lista para la respuesta
        representation = super(UltrasonidoSerializer, self).to_representation(instance)
        if instance.ruta_files:
            representation['ruta_files'] = json.loads(instance.ruta_files)
        else:
            representation['ruta_files'] = []
        # Eliminamos el campo 'ruta_files_list' en la respuesta ya que es solo para escritura
        representation.pop('ruta_files_list', None)
        return representation
class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model=Usuarios
        fields='__all__'

class DoctoresSerializer(serializers.ModelSerializer):
    class Meta:
        model=Doctor
        fields='__all__'