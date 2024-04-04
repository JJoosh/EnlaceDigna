import re
import secrets
import string
from django.utils import timezone
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import HttpResponse
from io import BytesIO
import numpy as np
from ..models import Cliente, Ultrasonidos, Usuarios
from .serializer import UltrasonidoSerializer
from .archivo import subir_archivo_a_s3, verificar_token
import json
from datetime import datetime
from PIL import Image
from .api_whatsapp import message_pedirToken
from io import BytesIO
from pydicom.pixel_data_handlers.util import apply_voi_lut
import pydicom
from moviepy.editor import VideoFileClip
import os
from ..models import EstadoUsuario
from .api_whatsapp import message_ayuda,enviar_galeria, enviar_gracias, enviarLista, enviar_cambioNumero, enviarMessage_errorToken
from .api_whatsapp import enviarToken_conNumero, enviar_pedirNumero, enviar_cambioNumero, enviarUltra_deLista
def convertir_avi_a_mp4(avi_path, mp4_path):
    """
    Convierte un archivo AVI a MP4.
    """
    clip = VideoFileClip(avi_path)
    clip.write_videofile(mp4_path)
    clip.close()

def convertir_gif_a_mp4(gif_path, mp4_path):
    """
    Convierte un archivo GIF a MP4.
    """
    clip = VideoFileClip(gif_path)
    clip.write_videofile(mp4_path)
    clip.close()

class UltrasonidoUploadAPIView(APIView):

    def post(self, request, *args, **kwargs):
        archivos = request.FILES.getlist('archivo')
        if not archivos:
            return Response({"mensaje": "No se encontraron archivos para subir."}, status=status.HTTP_400_BAD_REQUEST)
        
        rutas_files = []
        idPaciente = "Desconocido"
        nombrePaciente = "Desconocido"
        fechaUltrasonido = "Desconocido"
        descripcionUltras = "Desconocido"
        contador = 0
        
        # Obtener la ruta del directorio temporal
        ruta_temporal = os.environ.get('TEMP', '/tmp')  # Si no se encuentra, usa '/tmp' como valor predeterminado en sistemas Unix

        for archivo in archivos:
            extension = archivo.name.rsplit('.', 1)[-1].lower()
            if extension in ['jpeg', 'jpg']:
                # Procesamiento de archivos de imagen
                buffer = BytesIO(archivo.read())
                archivo_nombre = f"{archivo.name}"
                url = subir_archivo_a_s3(buffer, archivo_nombre, 'token_cliente')  # Asume manejo de tokens
                rutas_files.append(url)
            elif extension in ['mp4']:
                # Procesamiento de archivos de video MP4
                buffer = BytesIO(archivo.read())
                archivo_nombre = f"{archivo.name}"
                url = subir_archivo_a_s3(buffer, archivo_nombre, 'token_cliente')
                rutas_files.append(url)
            elif extension in ['avi']:
                # Procesamiento de archivos de video AVI
                avi_path = os.path.join(ruta_temporal, archivo.name)
                with open(avi_path, 'wb') as f:
                    f.write(archivo.read())
                
                mp4_path = os.path.join(ruta_temporal, os.path.splitext(archivo.name)[0] + '.mp4')
                convertir_avi_a_mp4(avi_path, mp4_path)
                
                with open(mp4_path, 'rb') as f:
                    buffer = BytesIO(f.read())
                archivo_nombre = f"{os.path.splitext(archivo.name)[0]}.mp4"
                url = subir_archivo_a_s3(buffer, archivo_nombre, )
                rutas_files.append(url)
                
                # Eliminar los archivos temporales
                os.remove(avi_path)
                os.remove(mp4_path)
            elif extension in ['dcm']:
                try:
                    dicom_data = pydicom.dcmread(archivo)
                    
                    if 'PixelData' in dicom_data:
                        # Procesamiento específico para archivos DICOM
                        image_data = self.procesar_dicom(dicom_data)
                        
                        # Verificar si es un volumen 3D o 4D
                        if 'NumberOfFrames' in dicom_data:
                            if dicom_data.NumberOfFrames > 1:
                                # Es un volumen 4D
                                gif_path = os.path.join(ruta_temporal, f"{archivo.name.rsplit('.', 1)[0]}.gif")
                                mp4_path = os.path.join(ruta_temporal, f"{archivo.name.rsplit('.', 1)[0]}.mp4")
                                self.convertir_volumen_a_gif(image_data, gif_path)
                                convertir_gif_a_mp4(gif_path, mp4_path)
                                
                                with open(mp4_path, 'rb') as f:
                                    buffer = BytesIO(f.read())
                                archivo_nombre = f"{archivo.name.rsplit('.', 1)[0]}.mp4"
                                url = subir_archivo_a_s3(buffer, archivo_nombre, fechaUltrasonido, idPaciente)  # Asume manejo de tokens
                                rutas_files.append(url)

                            else:
                                # Es un volumen 3D
                                gif_path = os.path.join(ruta_temporal, f"{archivo.name.rsplit('.', 1)[0]}.gif")
                                mp4_path = os.path.join(ruta_temporal, f"{archivo.name.rsplit('.', 1)[0]}.mp4")
                                self.convertir_volumen_a_gif(image_data, gif_path)
                                convertir_gif_a_mp4(gif_path, mp4_path)
                                
                                with open(mp4_path, 'rb') as f:
                                    buffer = BytesIO(f.read())
                                archivo_nombre = f"{archivo.name.rsplit('.', 1)[0]}.mp4"
                                url = subir_archivo_a_s3(buffer, archivo_nombre, fechaUltrasonido, idPaciente)
                                rutas_files.append(url)  # Asume manejo de tokens
                        else:
                            # Es una sola imagen 2D
                            jpeg_bytes = self.convertir_imagen_a_jpeg(image_data)
                            archivo_nombre_jpeg = f"{archivo.name.rsplit('.', 1)[0]}.jpeg"
                            buffer = BytesIO(jpeg_bytes)
                            url = subir_archivo_a_s3(buffer, archivo_nombre_jpeg, fechaUltrasonido, idPaciente)  # Asume manejo de tokens  # Asume manejo de tokens
                            rutas_files.append(url)
                        # Obtener datos DICOM
                        if contador == 0:
                            nombrePaciente, idPaciente, fechaUltrasonido, descripcionUltras = self.agarrar_datosDCM(dicom_data)
                            print("Nombre del paciente:", nombrePaciente)
                            print("Fecha del estudio:", fechaUltrasonido)
                            print("ID del paciente:", idPaciente)
                            print("Tipo de ultrasonido: ", descripcionUltras)
                        contador += 1
                except pydicom.errors.InvalidDicomError:
                    return Response({"mensaje": f"El archivo {archivo.name} no es un archivo DICOM válido."}, status=status.HTTP_400_BAD_REQUEST)
                except Exception as e:
                    return Response({"mensaje": f"Error procesando el archivo {archivo.name}: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                print(archivo, 'prueba')
                return Response({"mensaje": f"Tipo de archivo no soportado para {archivo.name}."}, status=status.HTTP_400_BAD_REQUEST)

        enviar_verificacion(idPaciente, nombrePaciente)  
        try:
            ultima_opcion_paciente = Ultrasonidos.objects.filter(cliente_id=idPaciente).latest('OpcionUltra')
            ultima_opcion_valor = ultima_opcion_paciente.OpcionUltra  # Obtener el valor de OpcionUltra del último objeto del paciente
        except Ultrasonidos.DoesNotExist:
            ultima_opcion_valor = 0

    # Incrementar el valor de OpcionUltra en 1
        nuevo_valor_opcion = ultima_opcion_valor + 1

            # Obtener la fecha actual
        fechaUltrasonido = timezone.now().strftime("%Y-%m-%d")

    # Crear un nuevo objeto Ultrasonidos con el nuevo valor de OpcionUltra
        ultrasonido_obj = Ultrasonidos.objects.create(ruta_files=json.dumps(rutas_files),
                                                  TipoDeUltrasonidos=descripcionUltras,
                                                  Fecha=fechaUltrasonido,
                                                  tokenUltrasonido=generar_token_10_caracteres(),
                                                  cliente_id=idPaciente,
                                                  OpcionUltra=nuevo_valor_opcion)
    
        serializer = UltrasonidoSerializer(ultrasonido_obj)
    
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    def procesar_dicom(self, dicom_data):
        # Apply necessary transformations to the DICOM image
        image_data = apply_voi_lut(dicom_data.pixel_array, dicom_data)

        # Convert to grayscale by taking the mean of RGB channels
        # Adjust pixel intensity range for better contrast
        

        # Check if it's a 3D or 4D volume
        if 'NumberOfFrames' in dicom_data:
            if dicom_data.NumberOfFrames > 1:
                
                image_data = image_data.mean(axis=-1)
                # Adjust pixel intensity range for better contrast
                min_val, max_val = np.percentile(image_data, (2, 98))
                image_data = np.clip(image_data, min_val, max_val)
                image_data = ((image_data - min_val) / (max_val - min_val)) * 255
                image_data = image_data.astype(np.uint8)
                return image_data
            else:
                image_data = image_data.mean(axis=-1)
                # Adjust pixel intensity range for better contrast
                min_val, max_val = np.percentile(image_data, (2, 98))
                image_data = np.clip(image_data, min_val, max_val)
                image_data = ((image_data - min_val) / (max_val - min_val)) * 255
                image_data = image_data.astype(np.uint8)
                return image_data
        else:
            min_val, max_val = np.percentile(image_data, (2, 98))
            image_data = np.clip(image_data, min_val, max_val)
            image_data = ((image_data - min_val) / (max_val - min_val)) * 255
            image_data = image_data.astype(np.uint8)
            
            return image_data


 
    def convertir_volumen_a_gif(self, volumen, gif_path):
        # Convierte un volumen (secuencia de imágenes numpy) a GIF
        frames = [Image.fromarray(imagen) for imagen in volumen]
        frames[0].save(gif_path, format='GIF', save_all=True, append_images=frames[1:], loop=0)

    def convertir_volumen_a_mp4(self, volumen, mp4_path):
        # Convierte un volumen (secuencia de imágenes numpy) a MP4
        frames = [Image.fromarray(imagen) for imagen in volumen]
        clip = VideoFileClip(fps=24, pixelsize=(frames[0].width, frames[0].height))
        for frame in frames:
            clip.write_frame(np.array(frame))
        clip.write_videofile(mp4_path)
        clip.close()


    def agarrar_datosDCM(self, dicom_data):
        try:
            # Obtener datos de las etiquetas DICOM relevantes
            paciente_nombre = dicom_data.PatientName if hasattr(dicom_data, 'PatientName') else "Desconocido"
            estudio_fecha = dicom_data.StudyDate if hasattr(dicom_data, 'StudyDate') else "Desconocido"
            paciente_id = dicom_data.PatientID if hasattr(dicom_data, 'PatientID') else "Desconocido"
            tipo_ultrasonido = dicom_data.Modality if hasattr(dicom_data, 'Modality') else "Desconocido"
            descripcion_ultrasonido = dicom_data.StudyDescription if hasattr(dicom_data, 'StudyDescription') else "Desconocido"
            return paciente_nombre, paciente_id, estudio_fecha, descripcion_ultrasonido

        except Exception as e:
            print("Error al procesar el archivo DICOM:", str(e))

    def convertir_imagen_a_jpeg(self, imagen):
        # Convierte una imagen numpy a JPEG
        with BytesIO() as output:
            if imagen.ndim == 2:
                # Si la imagen es de un solo canal (escala de grises), conviértela a RGB
                imagen = np.repeat(imagen[..., np.newaxis], 3, axis=-1)
            elif imagen.ndim == 3 and imagen.shape[-1] == 4:
                # Si la imagen tiene un canal alfa, elimínalo
                imagen = imagen[..., :3]
            
            Image.fromarray(imagen).convert('RGB').save(output, format='JPEG')
            jpeg_bytes = output.getvalue()
        return jpeg_bytes


def generar_token_10_caracteres():
    # Define el alfabeto para el token: letras (mayúsculas y minúsculas) y dígitos
    alfabeto = string.ascii_letters + string.digits
    # Genera un token de 10 caracteres aleatorios
    token = ''.join(secrets.choice(alfabeto) for _ in range(10))
    return token

def enviar_verificacion(cliente_id, nombrePaciente):
    data_cliente = get_object_or_404(Cliente, id=cliente_id)
    id_usuario = data_cliente.usuario.id
    print('Este es el id:', id_usuario)

    data_usuario = get_object_or_404(Usuarios, id=id_usuario)
    num_telefono = data_usuario.NumeroCelular
    print('Numero= ', num_telefono)
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
                            verificacion = verificar_token(mensaje, telefono)
                            if verificacion == False:
                                estado_usuario, created = EstadoUsuario.objects.get_or_create(telefono=telefono)
                                if estado_usuario.opcion_seleccionada == '5':
                                    enviarUltra_deLista(telefono[3:], mensaje)
                                    estado_usuario.opcion_seleccionada = None
                                    estado_usuario.save()
                                else:
                                    if mensaje == '1' or mensaje=="Hola" or mensaje=="hola" or mensaje=="HOLA":
                                        message_ayuda('52' + telefono[3:])
                                    
                                    elif mensaje == '2':
                                        enviar_galeria(telefono[3:])
                                    elif mensaje == '3':
                                        enviar_pedirNumero(telefono[3:])
                                    elif mensaje == '4':
                                        enviarToken_conNumero(telefono[3:])
                                    elif mensaje == 'gracias' or mensaje == 'Gracias' or mensaje == "GRACIAS":
                                        enviar_gracias(telefono[3:])
                                    elif mensaje == '5':
                                        estado_usuario.opcion_seleccionada = '5'
                                        estado_usuario.save()
                                        enviarLista(telefono[3:])
                                    elif len(mensaje) == 10 and mensaje.isdigit():
                                        enviar_cambioNumero(mensaje, telefono[3:])
                                    else:
                                        enviarMessage_errorToken('52' + telefono[3:])
                            else:
                                print('Mensaje recibido después de la solicitud POST. Ignorando.')
                        else:
                            print('Mensaje recibido después de la solicitud POST. Ignorando.')
        return Response({"status": "success"})

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
