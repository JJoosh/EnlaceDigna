# archivo.py

import boto3
from django.conf import settings

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
