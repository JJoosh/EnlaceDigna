from django.forms import ValidationError
from django.utils import timezone
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view  # Esta es la línea que falta
from django.http import HttpResponse
from pydicom import dcmread
from pydicom.errors import InvalidDicomError
from io import BytesIO
import numpy as np
from ..models import Cliente, Ultrasonidos, Usuarios  # Asegúrate de importar Usuarios

from .serializer import UltrasonidoSerializer
from .archivo import subir_archivo_a_s3, verificar_token  # Asegúrate de que verificar_token esté definido
import json
from datetime import datetime
from PIL import Image
import io
import magic

from io import BytesIO
import magic
from PIL import Image
from pydicom import dcmread
from pydicom.pixel_data_handlers.util import apply_voi_lut





class UltrasonidoUploadAPIView(APIView):
    # Asume que las permisiones y parsers necesarios están definidos aquí.

    def post(self, request, *args, **kwargs):
        archivos = request.FILES.getlist('archivo')
        if not archivos:
            return Response({"mensaje": "No se encontraron archivos para subir."}, status=status.HTTP_400_BAD_REQUEST)

        rutas_files = []
        for archivo in archivos:
            extension = archivo.name.rsplit('.', 1)[-1].lower()
            if extension in ['jpeg', 'jpg', 'mp4', 'avi']:
                buffer = BytesIO(archivo.read())
                archivo_nombre = f"{archivo.name}"
                url = subir_archivo_a_s3(buffer, archivo_nombre, 'token_cliente')  # Asume manejo de tokens
                rutas_files.append(url)
            elif extension in ['dcm']:
                try:
                    dicom_data = dcmread(archivo)
                    if 'PixelData' in dicom_data:
                        # Procesamiento específico para archivos DICOM
                        image_data = self.procesar_dicom(dicom_data)

                        # Convertir a imagen JPEG y guardar en buffer
                        pil_img = Image.fromarray(image_data)
                        buffer = BytesIO()
                        pil_img.save(buffer, format="JPEG")
                        buffer.seek(0)  # Rebobinar el buffer

                        # Construir nombre de archivo y subir a S3
                        archivo_nombre_jpeg = f"{archivo.name.rsplit('.', 1)[0]}.jpeg"
                        url = subir_archivo_a_s3(buffer, archivo_nombre_jpeg, 'token_cliente')  # Asume manejo de tokens
                        rutas_files.append(url)
                    else:
                        return Response({"mensaje": f"El archivo {archivo.name} no contiene datos de imagen."}, status=status.HTTP_400_BAD_REQUEST)
                except InvalidDicomError:
                    return Response({"mensaje": f"El archivo {archivo.name} no es un archivo DICOM válido."}, status=status.HTTP_400_BAD_REQUEST)
                except Exception as e:
                    return Response({"mensaje": f"Error procesando el archivo {archivo.name}: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"mensaje": f"Tipo de archivo no soportado para {archivo.name}."}, status=status.HTTP_400_BAD_REQUEST)

        ultrasonido_obj = Ultrasonidos.objects.create(ruta_files=json.dumps(rutas_files))
        serializer = UltrasonidoSerializer(ultrasonido_obj)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def procesar_dicom(self, dicom_data):
        # Aplicar transformaciones necesarias a la imagen DICOM
        image_data = apply_voi_lut(dicom_data.pixel_array, dicom_data)
        if dicom_data.PhotometricInterpretation == "MONOCHROME1":
            image_data = np.amax(image_data) - image_data
        image_data = (np.clip(image_data, 0, None) / image_data.max()) * 255.0
        image_data = np.uint8(image_data)
        return image_data



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
                        if timestamp_mensaje <= timestamp_solicitud:
                            print('Procesando mensaje:', mensaje)
                            print('Procesando teléfono:', telefono)
                            return verificar_token(mensaje, telefono)
                        else:
                            print('Mensaje recibido antes de la solicitud POST. Ignorando.')
 
        return Response({"status": "success"})

<<<<<<< HEAD
# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     def validate(self, attrs):
#         data = super().validate(attrs)
#         user = self.user  # El usuario ya está disponible aquí
#         if user.rol != 'Doctor':
#             raise serializers.ValidationError('Solo los doctores pueden acceder.')
#         return data

# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer
=======

@api_view(['GET'])
def get_galeria(request, token):
    try:
        cliente = Cliente.objects.get(Token=token)
        datos_ultrasonido = Ultrasonidos.objects.filter(cliente=cliente)
        
        data = [{'ruta_files': ultrasonido.ruta_files, 'TipoDeUltrasonidos': ultrasonido.TipoDeUltrasonidos, 'Fecha': ultrasonido.Fecha} for ultrasonido in datos_ultrasonido]
        return Response(data)
    
    except Cliente.DoesNotExist:
        return Response({'error': 'El token proporcionado no corresponde a ningún cliente'}, status=404)
    except Ultrasonidos.DoesNotExist:
        return Response({'error': 'No se encontraron ultrasonidos para este cliente'}, status=404)
>>>>>>> 4aec583b7a77517d3bf1890cd22d4580abbacbf1
