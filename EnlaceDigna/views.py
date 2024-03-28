from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import Usuario, Cliente  # Importa correctamente tu modelo Usuario

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Crear un nuevo usuario con los datos del formulario
            nuevo_usuario = Usuario(
                Nombre=form.cleaned_data['name'],
                Apellido_Paterno=form.cleaned_data['apellido_paterno'],
                Apellido_Materno=form.cleaned_data.get('apellido_materno', ''),
                Correo=form.cleaned_data['email'],
                NumeroCelular=form.cleaned_data.get('number', ''),
                Rol=form.cleaned_data['rol']  # Asegúrate de que el formulario tenga un campo 'rol'
            )
            nuevo_usuario.save()  # Guardar el nuevo usuario en la base de datos
            
            # Redirige a una nueva URL tras el éxito
            return redirect('dashboard')  # Asegúrate de reemplazar 'success_url_name'
    else:
        form = RegisterForm()

    return render(request, 'index.html', {'form': form})


def dashboard(request):
    query = request.GET.get('search', '')  # Obtiene el parámetro de búsqueda 'search' de la URL, si existe
    clientes_encontrados = Cliente.objects.select_related('usuario')
    clientes = clientes_encontrados.filter(Token__icontains=query) if query else None

    # Indicador de si se ha realizado una búsqueda.
    search_performed = bool(query and clientes)

    context = {
        'clientes': clientes if search_performed else None,  # Solo pasamos los clientes si se realizó una búsqueda
        'query': query,
        'search_performed': search_performed,  # Indicador de búsqueda realizada
        'todos_los_clientes': clientes_encontrados if not search_performed else None,  # Lista de todos los clientes si no se realizó búsqueda
    }

    return render(request, 'dashboard.html', context)

