from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import Usuarios, Cliente  # Importa correctamente tu modelo Usuario
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login
from django.contrib import messages


@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Crear un nuevo usuario con los datos del formulario
            nuevo_usuario = Usuarios(
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

@csrf_protect
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

@csrf_protect
def galeria(request):
    return render(request, 'galeria.html')




def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')  # Asegurándonos de capturar la contraseña también

        # Primero, intentamos autenticar al usuario por email y contraseña
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            # Aquí, asumimos que `EnlaceDigan_usuario` está relacionado de alguna manera con el usuario
            # Vamos a buscar la instancia de EnlaceDigan_usuario que coincida con este usuario
            try:
                user_link = EnlaceDigan_usuario.objects.get(user=user)
                if user_link.Rol == 'Doctor':
                    login(request, user)
                    return redirect('dashboard')
                else:
                    messages.error(request, 'Acceso denegado. Solo los doctores pueden ingresar.')
            except EnlaceDigan_usuario.DoesNotExist:
                messages.error(request, 'No se encontró el enlace de usuario correspondiente.')
        else:
            messages.error(request, 'Correo electrónico o contraseña inválidos.')
    else:
        # Manejo del caso para métodos que no son POST
        pass

    return render(request, 'login1.html', {})