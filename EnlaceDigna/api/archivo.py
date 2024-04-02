# archivo.py

import os
from urllib.parse import quote_plus
import boto3
from django.conf import settings
from django.shortcuts import get_object_or_404
import requests
import urllib.request
from ..models import Cliente
from rest_framework.response import Response
from rest_framework import status
from .api_whatsapp import enviar_mensaje
from django.core.exceptions import ObjectDoesNotExist
from .api_whatsapp import enviarMessage_errorToken
from ..models import Usuarios, Ultrasonidos
import magic

def verificar_token(token, num):
    data_cliente = Cliente.objects.filter(Token=token).first()

    if data_cliente is None:
        print('Token no encontrado')
        return enviarMessage_errorToken('52' + num[3:])

    id_usuario = data_cliente.usuario_id

    data_usuario = Usuarios.objects.filter(id=id_usuario).first()

    if data_usuario and data_usuario.NumeroCelular == num[3:]:
        print('Usuario encontrado:', data_usuario)

        urlimg , urlvideo= buscar_urls(data_cliente.id)

        print('img:', urlimg)
        print('video', urlvideo)
  
        return enviar_mensaje('52' + data_usuario.NumeroCelular, data_usuario.Nombre, data_usuario.Apellido_Paterno, urlvideo, urlimg)
    else:
        print('Usuario no encontrado')
        return enviarMessage_errorToken(num[3:])



from urllib.parse import quote
import boto3
from django.conf import settings


def subir_archivo_a_s3(buffer, nombre_archivo, token):
    # Codifica solo los caracteres necesarios con quote_plus, lo que resultará en %20 para los espacios
    nombre_archivo_codificado = quote_plus(nombre_archivo)

    ruta_s3 = f"ultrasonidos/{nombre_archivo_codificado}"

    s3 = boto3.client(
        's3',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    )

    # Determina el tipo de contenido del archivo
    file_type = magic.from_buffer(buffer.read(2048), mime=True)
    buffer.seek(0)  # Rebobinar el buffer

    # Sube el archivo con el nombre original y el tipo de contenido
    s3.upload_fileobj(
        buffer,
        settings.AWS_STORAGE_BUCKET_NAME,
        ruta_s3,
        ExtraArgs={
            "ACL": "public-read",
            "ContentType": file_type
        }
    )

    # Genera la URL sin recodificar el nombre del archivo
    url = f"https://{settings.AWS_S3_CUSTOM_DOMAIN}/{ruta_s3}"
    return url



def buscar_urls(id):
    data_ultrasonidos = Ultrasonidos.objects.filter(cliente=id).last()


    urls = data_ultrasonidos.ruta_files

    urlimg = []
    urlvid = []

    # Eliminar corchetes y comillas dobles y luego dividir la cadena en una lista
    url_list = [x.strip('"') for x in urls.strip('[]').split(', ')]
    extensiones_validasimg = ['jpeg', 'jpg', 'png', 'svg']
    extensiones_validas_video = ['mp4', 'avi', 'mov', 'mkv', 'wmv', 'flv', 'mpeg']

    for url in url_list:
        print('url sola:', url)
        parts = url.split('.')
        if parts[-1] in extensiones_validasimg:
            urlimg.append(url)
        elif parts[-1] in extensiones_validas_video:
            urlvid.append(url)

    print(urlimg)
    print(urlvid)
    return urlimg, urlvid
