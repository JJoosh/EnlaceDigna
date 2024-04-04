from ..models import Usuarios
from ..models import Cliente
from ..models import Ultrasonidos
def verificarNumeroParaCorreo(numero):
    try:
        data_usser=Usuarios.objects.get(NumeroCelular=numero)
        print(data_usser.Correo)
        return True
    
    except:
        print("maaaal")
        return False
    

def verificar_DevolverLista(numero):
    try:
        data = []
        data_usuario = Usuarios.objects.get(NumeroCelular=numero)
        cliente = Cliente.objects.get(usuario=data_usuario)

        ultrasonidos_queryset = Ultrasonidos.objects.filter(cliente=cliente)
        if ultrasonidos_queryset.exists():
            for ultrasonido in ultrasonidos_queryset:
                print('Tipo de ultrasonido:', ultrasonido.TipoDeUltrasonidos)
                print('Fecha de ultrasonido:', ultrasonido.Fecha)
                print('Opción Ultra:', ultrasonido.OpcionUltra)
                data.append((str(ultrasonido.OpcionUltra)+"-" , ultrasonido.TipoDeUltrasonidos, ultrasonido.Fecha))
            return data
        else:
            print("No se encontraron ultrasonidos para este cliente.")
    except Exception as e:
        print("Algo salió mal:", e)



def ObtenerToken(numero):
    data_usser=Usuarios.objects.get(NumeroCelular=numero)
    return data_usser.id



def separarURL(urls):
    url_list = [x.strip('"') for x in urls.strip('[]').split(', ')]
    urlImg=[]
    urlVideo=[]
    extensiones_validasimg = ['jpeg', 'jpg', 'png', 'svg', 'gif']
    extensiones_validas_video = ['mp4', 'avi', 'mov', 'mkv', 'wmv', 'flv', 'mpeg']

    for url in url_list:
        print('url sola:', url)
        parts = url.split('.')
        if parts[-1] in extensiones_validasimg:
            urlImg.append(url)
        elif parts[-1] in extensiones_validas_video:
            urlVideo.append(url)

    return urlImg, urlVideo


def ObtenerURL_Opcion(opcion):
    dataUltra=Ultrasonidos.objects.filter(OpcionUltra=opcion).first()
    urls=dataUltra.ruta_files
    fecha=dataUltra.Fecha
    nombre=dataUltra.TipoDeUltrasonidos
    return urls, fecha, nombre
