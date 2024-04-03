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

        data=[]
        data_usuario = Usuarios.objects.get(NumeroCelular=numero)
        cliente = Cliente.objects.get(usuario=data_usuario)

        ultrasonidos_queryset = Ultrasonidos.objects.filter(cliente=cliente)
        if ultrasonidos_queryset.exists():
            for ultrasonido in ultrasonidos_queryset:
                print('Tipo de ultrasonido: ' ,ultrasonido.TipoDeUltrasonidos)
                print('Fecha de ultrasonido: ' ,ultrasonido.Fecha)
                data.append((ultrasonido.TipoDeUltrasonidos, ultrasonido.Fecha))
            return data
        else:
            print("No se encontraron ultrasonidos para este cliente.")
    except Exception as e:
        print("Algo salió mal:", e)
