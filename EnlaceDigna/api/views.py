from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .serializer import UltrasonidoSerializer  # Asegúrate de que el nombre del serializer coincida
from .archivo import subir_archivo_a_s3  # Ajusta el import según tu estructura de proyecto
from rest_framework.decorators import api_view
from ..models import Usuarios
from .api_whatsapp import message_pedirToken
import requests
import json
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .archivo import verificar_token
from django.forms import ValidationError
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from ..models import Ultrasonidos, Cliente  # Asumiendo que Cliente está en el mismo lugar que Ultrasonido
from .serializer import UltrasonidoSerializer
from .archivo import subir_archivo_a_s3
import json
import re
import logging



from datetime import datetime, timedelta

import hashlib

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
        print(archivos)
        for archivo in archivos:
            logging.debug(f"Procesando archivo: {archivo.name}")
            nombre_archivo_sanitizado = archivo.name.replace(" ", "+")
            nombre_archivo = f'{nombre_archivo_sanitizado}'  # Directamente el token del cliente como carpeta principal
            url = subir_archivo_a_s3(archivo, nombre_archivo, token_cliente)  # Asegúrate de que esta función acepte el token como argumento
            rutas_files.append(url)

        rutas_files_json = json.dumps(rutas_files)

        try:
            ultrasonido_obj = Ultrasonidos.objects.create(
                ruta_files=rutas_files_json,
                cliente_id=id_cliente,
                TipoDeUltrasonidos=tipo_ultrasonido,
                Fecha=fecha_actual
            )
        except ValidationError as e:
            return Response({"mensaje": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        serializer = UltrasonidoSerializer(ultrasonido_obj)
        return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(['POST', 'GET'])
def enviar_verificacion(request, cliente_id):

   
    data_cliente = get_object_or_404(Cliente, id=cliente_id)
    id_usuario = data_cliente.usuario_id
    print('Este es el id:', id_usuario)

    data_usuario = get_object_or_404(Usuarios, id=id_usuario)
    num_telefono = data_usuario.NumeroCelular
    nombre = data_usuario.Nombre
    codigo_area = '52'
    print(nombre, ' asdasd',  codigo_area + num_telefono)                                                      
    return message_pedirToken(codigo_area + num_telefono, nombre)


@api_view(['POST', 'GET'])
def recibir_tokenWhats(request):
    if request.method == "GET":
        if request.GET.get('hub.verify_token') == "12345":
            return HttpResponse(request.GET.get('hub.challenge'))
        else:
            return Response({"error": "Error de autenticación."}, status=403)

    if request.method == 'POST':
        data = request.data
        timestamp_solicitud = datetime.now()
        if 'entry' in data and data['entry']:
            entry = data['entry'][0]
            if 'changes' in entry:
                change = entry['changes'][0]
                value = change.get('value', {})
                messages = value.get('messages', [])
                if messages:
                    message = messages[0]
                    mensaje = message.get('text', {}).get('body')
                    telefono = message.get('from')
                    timestamp_mensaje = message.get('timestamp')
                    if mensaje and telefono and timestamp_mensaje:
                        timestamp_mensaje = datetime.fromtimestamp(int(timestamp_mensaje))
                        if timestamp_mensaje >= timestamp_solicitud:
                            print('Procesando mensaje:', mensaje)
                            print('Procesando teléfono:', telefono)
                            return verificar_token(mensaje, telefono)
                        else:
                            print('Mensaje recibido antes de la solicitud POST. Ignorando.')
 
        return Response({"status": "success"})