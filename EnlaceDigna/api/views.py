from django.forms import ValidationError
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from ..models import Ultrasonido, Cliente  # Asumiendo que Cliente está en el mismo lugar que Ultrasonido
from .serializer import UltrasonidoSerializer
from .archivo import subir_archivo_a_s3
import json
import re
import logging

class UltrasonidoUploadAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        archivos = request.FILES.getlist('archivo')
        if not archivos:
            return Response({"mensaje": "No se encontraron archivos para subir."}, status=status.HTTP_400_BAD_REQUEST)

        tipo_ultrasonido = request.data.get('ultrasonido')
        id_cliente = request.data.get('cliente_id')
        fecha_actual = timezone.now().date()

        if not tipo_ultrasonido:
            return Response({"mensaje": "El tipo de ultrasonido es requerido."}, status=status.HTTP_400_BAD_REQUEST)
        
        if not re.match(r'^[A-Za-z\s]+$', tipo_ultrasonido):
            return Response({"mensaje": "El tipo de ultrasonido contiene caracteres inválidos."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            cliente = Cliente.objects.get(id=id_cliente)
            token_cliente = cliente.Token
        except Cliente.DoesNotExist:
            return Response({"mensaje": "Cliente no encontrado."}, status=status.HTTP_404_NOT_FOUND)
        except Cliente.MultipleObjectsReturned:
            return Response({"mensaje": "Múltiples clientes encontrados con el mismo ID."}, status=status.HTTP_400_BAD_REQUEST)

        rutas_files = []
        for archivo in archivos:
            logging.debug(f"Procesando archivo: {archivo.name}")
            nombre_archivo_sanitizado = archivo.name.replace(" ", "+")
            nombre_archivo = f'{nombre_archivo_sanitizado}'  # Directamente el token del cliente como carpeta principal
            url = subir_archivo_a_s3(archivo, nombre_archivo, token_cliente)  # Asegúrate de que esta función acepte el token como argumento
            rutas_files.append(url)

        rutas_files_json = json.dumps(rutas_files)

        try:
            ultrasonido_obj = Ultrasonido.objects.create(
                ruta_files=rutas_files_json,
                cliente_id=id_cliente,
                TipoDeUltrasonidos=tipo_ultrasonido,
                Fecha=fecha_actual
            )
        except ValidationError as e:
            return Response({"mensaje": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        serializer = UltrasonidoSerializer(ultrasonido_obj)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
