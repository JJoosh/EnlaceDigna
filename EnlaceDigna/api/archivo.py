# archivo.py

from urllib.parse import quote_plus
import boto3
from django.conf import settings
from .api_whatsapp import enviar_mensaje
from ..models import Usuarios, Ultrasonidos
import magic

def verificar_token(token, num):
    data_cliente = Ultrasonidos.objects.filter(tokenUltrasonido=token).first()
    print(data_cliente ,'data cliente')
    if data_cliente is None:
        print('Token no encontrado')
        return False

    id_usuario =data_cliente.cliente.id
    print('id cliente= ' , id_usuario)
    data_usuario = Usuarios.objects.filter(id=id_usuario).first()

    if data_usuario and data_usuario.NumeroCelular == num[3:]:
        print('Usuario encontrado:', data_usuario)

        urlimg , urlvideo= buscar_urls(id_usuario)
        print('img:', urlimg)
        print('video', urlvideo)
        return enviar_mensaje('52' + data_usuario.NumeroCelular, data_usuario.Nombre, data_usuario.Apellido_Paterno, urlvideo, urlimg, data_cliente.TipoDeUltrasonidos, str(data_cliente.Fecha))
    else:
        print('Usuario no encontrado')
        return False


def subir_archivo_a_s3(buffer, nombre_archivo, fecha, idcliente):
    nombre_archivo_codificado = quote_plus(nombre_archivo)

    ruta_carpeta_cliente = f"ultrasonidos/{idcliente}/{fecha}/"

    s3 = boto3.client(
        's3',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    )

    # Verifica si la carpeta ya existe
    try:
        s3.head_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key=ruta_carpeta_cliente)
    except:
        # Si la carpeta no existe, la crea
        s3.put_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key=ruta_carpeta_cliente)

    ruta_s3 = ruta_carpeta_cliente + nombre_archivo_codificado

    file_type = magic.from_buffer(buffer.read(2048), mime=True)
    buffer.seek(0)  

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

    # Elimina corchetes y comillas dobles y luego dividir la cadena en una lista
    url_list = [x.strip('"') for x in urls.strip('[]').split(', ')]
    extensiones_validasimg = ['jpeg', 'jpg', 'png', 'svg', 'gif']
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


