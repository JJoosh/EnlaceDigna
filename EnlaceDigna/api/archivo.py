# archivo.py

import os
import boto3
from django.conf import settings
import requests
import urllib.request

def subir_archivo_a_s3(archivo, nombre_archivo):
    s3 = boto3.client(
        's3',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    )

    s3.upload_fileobj(
        archivo,
        settings.AWS_STORAGE_BUCKET_NAME,
        nombre_archivo,
        ExtraArgs={
            "ACL": "public-read",
            "ContentType": archivo.content_type
        }
    )
    nombre_archivo=nombre_archivo.replace(' ','+')
    url = f"https://{settings.AWS_S3_CUSTOM_DOMAIN}/{nombre_archivo}"
    return url

#AQUI DESCARGARA EL ARCHIVO Y LO ENVIARA POR WHATHSAPP
def download_archivo(telefono, url, nombre):

    for url in url:
        parts = url.split('/')
        nombre_archivo = parts[-1]
        urllib.request.urlretrieve(url, nombre_archivo)
        
        send_archivo(telefono)

        os.remove(nombre_archivo)


def send_archivo(telefono):
    
    numtelefono=''

