from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from ..models import Ultrasonidos  # Asegúrate de ajustar este importe según la ubicación de tu modelo
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



from datetime import datetime, timedelta

import hashlib

class UltrasonidoUploadAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        archivo = request.FILES.get('archivo')
        if archivo is None:
            return Response({"mensaje": "No se encontró archivo para subir."}, status=status.HTTP_400_BAD_REQUEST)
        
        
        id_usuario = request.data.get('ID')  # Asegúrate de que este sea el ID del usuario
        print("ACA ESTA EL PEDO")
        print(id_usuario)

        nombre_archivo = 'ultrasonidos/' + archivo.name
        ruta_files = subir_archivo_a_s3(archivo, nombre_archivo)  # Asumiendo que esta función retorna la URL del archivo
        
        # Crear instancia del modelo Ultrasonidos con la información proporcionada y guardar
        ultrasonido_obj = Ultrasonidos.objects.create(
            ruta_files=ruta_files,
            id_usuario_id=id_usuario,  # Cambio aquí para reflejar la relación FK correctamente
            tipo_ultrasonido="Cancer",
            fecha='2003-12-02'
        )
        serializer = UltrasonidoSerializer(ultrasonido_obj)  # Asegúrate de que el serializer exista y esté correctamente definido
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(['GET'])
def enviar_verificacion(request, token):

    Datausuario = get_object_or_404(Usuarios, token=token)
    numTelefono=Datausuario.numero_telefono
    nombre=Datausuario.nombre
    codeArea='52'
    print(nombre, ' asdasd',  codeArea+numTelefono)                                                      
    return message_pedirToken(codeArea+numTelefono, nombre)



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