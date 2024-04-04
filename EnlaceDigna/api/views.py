from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import SimpleITK as sitk
import tempfile
import os
from datetime import datetime
import random
import string

from EnlaceDigna.api.api_whatsapp import enviarUltra_deLista, message_pedirToken
from ..models import EstadoUsuario, Ultrasonidos, Cliente, Usuarios
from .archivo import subir_archivo_a_s3, verificar_token
from .serializer import UltrasonidoSerializer
import json
import shutil
import imageio
from rest_framework.decorators import api_view
from .api_whatsapp import message_ayuda,enviar_galeria, enviar_gracias, enviarLista, enviar_cambioNumero, enviarMessage_errorToken
from .api_whatsapp import enviarToken_conNumero, enviar_pedirNumero, enviar_cambioNumero, enviarUltra_deLista



class UltrasonidoUploadAPIView(APIView):
    def post(self, request, format=None):
        print(request)
        archivos = request.FILES.getlist('archivo')
        if not archivos:
            return Response({'error': 'No se han enviado archivos'}, status=status.HTTP_400_BAD_REQUEST)

        rutas_files = []
        metadatos_files = []
        
        for file in archivos:
            temp_file_path = None
            try:
                with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                    for chunk in file.chunks():
                        temp_file.write(chunk)
                    temp_file_path = temp_file.name
                
                image = sitk.ReadImage(temp_file_path)
                metadata = {key: image.GetMetaData(key) for key in image.GetMetaDataKeys()}
                metadatos_files.append(metadata)
                id_cliente = metadata.get('0010|0020')
                TipoUltrasonido = metadata.get('0008|1030')
                if not id_cliente:
                    return Response({'error': 'No se ha encontrado el ID del cliente en los metadatos del DICOM'}, status=status.HTTP_400_BAD_REQUEST)

                dimension = image.GetDepth()
                print(dimension)

                nombre_archivo_sin_espacios = file.name.replace(' ', '')

                # Crear una carpeta para guardar los archivos
                output_folder = tempfile.mkdtemp()
                
                # Iterar sobre los frames y guardarlos como imágenes JPEG si es 2D,
                # o crear un video MP4 si es 3D o 4D
                
                if dimension == 1:
                    print(dimension)
                    image_files = []
                    for i in range(image.GetDepth()):
                        image_slice = image[:, :, i]
                        image_array = sitk.GetArrayFromImage(image_slice)
                        # Guardar el frame como una imagen JPEG
                        output_path = os.path.join(output_folder, f'frame_{i:04d}.jpg')
                        sitk.WriteImage(image_slice, output_path)
                        image_files.append(output_path)
    
                    # Subir las imágenes JPEG a Amazon S3
                    for image_file in image_files:
                        with open(image_file, 'rb') as data:
                            fecha = datetime.now().date().strftime('%Y-%m-%d')
                            jpeg_filename = os.path.basename(image_file)
                            url = subir_archivo_a_s3(data, jpeg_filename, fecha, id_cliente)
                            rutas_files.append(url)
                else:
                    image_files = []
                    for i in range(image.GetDepth()):
                        if dimension == 4:
                            image_slice = image[:, :, :, i]
                        else:
                            image_slice = image[:, :, i]
                        image_array = sitk.GetArrayFromImage(image_slice)
                        # Guardar el frame como una imagen PNG
                        output_path = os.path.join(output_folder, f'frame_{i:04d}.png')
                        sitk.WriteImage(image_slice, output_path)
                        image_files.append(output_path)

                    # Crear el video MP4 a partir de las imágenes utilizando imageio
                    mp4_filename = nombre_archivo_sin_espacios.rsplit('.', 1)[0] + ".mp4"
                    temp_mp4_path = os.path.join(tempfile.gettempdir(), mp4_filename)
                    with imageio.get_writer(temp_mp4_path, format='FFMPEG', mode='I', fps=10) as writer:
                        for image_file in image_files:
                            writer.append_data(imageio.imread(image_file))

                    with open(temp_mp4_path, 'rb') as data:
                        fecha = datetime.now().date().strftime('%Y-%m-%d')
                        url = subir_archivo_a_s3(data, mp4_filename, fecha, id_cliente)
                        rutas_files.append(url)
                    os.remove(temp_mp4_path)

            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            finally:
                if temp_file_path and os.path.exists(temp_file_path):
                    os.remove(temp_file_path)  # Ensure the temporary file is cleaned up
                if os.path.exists(output_folder):
                    shutil.rmtree(output_folder)  # Ensure the temporary folder is cleaned up

        cliente, created = Cliente.objects.get_or_create(id=id_cliente)
        token = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        data = Ultrasonidos.objects.filter(cliente=id_cliente).last()
        if data:
             ultimo_valor_opcion = data.OpcionUltra + 1
        else:
            ultimo_valor_opcion = 0
        ultrasonido_obj = Ultrasonidos.objects.create(
            ruta_files=json.dumps(rutas_files),
            TipoDeUltrasonidos=TipoUltrasonido,
            Fecha=datetime.now().date(),
            tokenUltrasonido=token,
            cliente=cliente,
            OpcionUltra=ultimo_valor_opcion
        )

        serializer = UltrasonidoSerializer(ultrasonido_obj)
        enviar_verificacion(id_cliente)

        response_data = {
            'data': serializer.data,
            'metadata': metadatos_files
        }

        return Response(response_data, status=status.HTTP_200_OK)



def enviar_verificacion(cliente_id):
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
def receive_messages(request):
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
                        if timestamp_mensaje < timestamp_solicitud :
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
                                print('Mensaje recibido antes de la solicitud POST. Ignorando.')
                        else:
                            print('Mensaje recibido después de la solicitud POST. Ignorando.')
        return Response({"status": "success"})

@api_view(['GET'])
def get_galeria(request, id):
    try:
        cliente = Cliente.objects.get(id=id)
        datos_ultrasonido = Ultrasonidos.objects.filter(cliente=cliente)
        
        data = [{'ruta_files': ultrasonido.ruta_files, 'TipoDeUltrasonidos': ultrasonido.TipoDeUltrasonidos, 'Fecha': ultrasonido.Fecha} for ultrasonido in datos_ultrasonido]
        return Response(data)
    
    except Cliente.DoesNotExist:
        return Response({'error': 'El token proporcionado no corresponde a ningún cliente'}, status=404)
    except Ultrasonidos.DoesNotExist:
        return Response({'error': 'No se encontraron ultrasonidos para este cliente'}, status=404)