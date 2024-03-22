from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from ..models import Ultrasonidos  # Asegúrate de ajustar este importe según la ubicación de tu modelo
from .serializer import UltrasonidoSerializer  # Asegúrate de que el nombre del serializer coincida
from .archivo import subir_archivo_a_s3  # Ajusta el import según tu estructura de proyecto

class UltrasonidoUploadAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        archivo = request.FILES.get('archivo')
        if archivo is None:
            return Response({"mensaje": "No se encontró archivo para subir."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Suponiendo que necesitas los siguientes datos del request
        # tipo_ultrasonido = request.data.get('tipo_ultrasonido')
        # fecha = request.data.get('fecha')  # Asegúrate de que la fecha se envíe en un formato que Django pueda parsear correctamente
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
