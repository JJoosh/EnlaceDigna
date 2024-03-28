# archivo.py

import os
import boto3
from django.conf import settings
import requests
import urllib.request
from ..models import Usuarios
from rest_framework.response import Response
from rest_framework import status
from .api_whatsapp import enviar_mensaje
from django.core.exceptions import ObjectDoesNotExist
from .api_whatsapp import enviarMessage_errorToken
from .serializer import UsuariosSerializer

def verificar_token(token, num):
    usuario = Usuarios.objects.filter(token=token).first()
    if usuario and usuario.numero_telefono==num[3:]:
        serializer = UsuariosSerializer(usuario)
        data = serializer.data
        print('Usuario encontrado:', data)
        enviar_mensaje('52' + data['numero_telefono'], data['nombre'], data['apellido_p'])
        return Response({'envio correcto?': True})
    else:
        print('Usuario no encontrado')
        return enviarMessage_errorToken('52'+num[3:])
    
           
    


def subir_archivo_a_s3(archivo, nombre_archivo, token):
    # Reemplazar espacios en blanco en el nombre del archivo para evitar problemas con la URL
    nombre_archivo = nombre_archivo.replace(' ', '+')

    # La ruta del archivo en S3 ahora solo incluirá el token como nombre de carpeta
    ruta_s3 = f"ultrasonidos/{token}/{nombre_archivo}" 

    s3 = boto3.client(
        's3',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    )

    s3.upload_fileobj(
        archivo,
        settings.AWS_STORAGE_BUCKET_NAME,
        ruta_s3,
        ExtraArgs={
            "ACL": "public-read",
            "ContentType": archivo.content_type
        }
    )

    # La URL que se retorna incluirá la ruta completa con el token como carpeta
    url = f"https://{settings.AWS_S3_CUSTOM_DOMAIN}/{ruta_s3}"
    return url




def buscar_urls():
    
    return 1

