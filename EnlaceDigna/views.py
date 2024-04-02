from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.cache import cache
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password, check_password
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed 
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication

from .forms import RegisterForm
from .models import Usuarios, Cliente

import secrets
import random
# Para el registro de usuarios
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Asegúrate de hashear la contraseña antes de guardarla
            hashed_password = make_password(form.cleaned_data['password'])
            nuevo_usuario = Usuarios(
                Nombre=form.cleaned_data['name'],
                Apellido_Paterno=form.cleaned_data['apellido_paterno'],
                Apellido_Materno=form.cleaned_data.get('apellido_materno', ''),
                Correo=form.cleaned_data['email'],
                Password=hashed_password,  # Usa la contraseña hasheada
                NumeroCelular=form.cleaned_data.get('number', ''),
                Rol=form.cleaned_data['rol']
            )
            nuevo_usuario.save()
            # Asegúrate de redirigir al usuario a la página de login tras registrarse
            return redirect('login_view')  # Asumiendo que 'login_view' es el nombre de tu URL de login
    else:
        form = RegisterForm()
    return render(request, 'index.html', {'form': form})
def login_view(request):
    if request.method == 'GET':
        return render(request, 'login1.html')
    elif request.method == 'POST':
        email = request.POST.get('email')
        access_code = request.POST.get('access_code', None)

        if not access_code:
            token = get_unique_token()
            send_email_with_token(email, token)
            cache.set(email, token, timeout=300)
            return JsonResponse({'message': 'Revisa tu correo electrónico para el código de acceso.'})
        
        saved_token = cache.get(email)
        if saved_token and saved_token == access_code:
            user = Usuarios.objects.get(Correo=email)
            refresh = RefreshToken.for_user(user)

            # Almacena el token de acceso en la sesión
            request.session['access_token'] = str(refresh.access_token)
            
            # Redirige al usuario a la vista del dashboard
            return HttpResponseRedirect(reverse('dashboard_view'))  # Asegúrate de que 'dashboard_view' sea el nombre correcto de la ruta en tu archivo urls.py
        else:
            return JsonResponse({'error': 'Correo electrónico o código de acceso inválido.'}, status=400)
def dashboard_view(request):
    # Obtiene el token de la sesión
    raw_token = request.session.get('access_token', None)
    if raw_token:
        try:
            # Utiliza JWTAuthentication para obtener el usuario y el token verificado
            jwt_authentication = JWTAuthentication()
            validated_token = jwt_authentication.get_validated_token(raw_token)
            user = jwt_authentication.get_user(validated_token)
            
            # Verifica si el usuario está autenticado
            if user and user.is_authenticated:
                query = request.GET.get('search', '')
                clientes_encontrados = Cliente.objects.select_related('usuario')
                clientes = clientes_encontrados.filter(Token__icontains=query) if query else clientes_encontrados
                search_performed = bool(query and clientes)

                context = {
                    'clientes': clientes,
                    'query': query,
                    'search_performed': search_performed,
                    'todos_los_clientes': list(clientes_encontrados.values()) if not search_performed else None,
                }

                return render(request, 'dashboard.html', context)
        except AuthenticationFailed:
            # Maneja el caso en que la autenticación falla
            return HttpResponseRedirect(settings.LOGIN_URL)
    else:
        # Si no hay token en la sesión, redirige al login
        return HttpResponseRedirect(settings.LOGIN_URL)

def get_unique_token(length=6):
    # Generar un número aleatorio de 'length' dígitos y convertirlo a string
    # El rango va de 10^(length-1) para asegurar el mínimo de dígitos
    # hasta (10^length)-1 para asegurar el máximo de dígitos
    range_start = 10**(length-1)
    range_end = (10**length)-1
    token = random.randint(range_start, range_end)
    return str(token)

def send_email_with_token(email, token):
    subject = 'Tu Código de Acceso'
    message = f'Usa el siguiente código para iniciar sesión: {token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)


# def login_request(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         token = get_unique_token()
#         send_email_with_token(email, token)
#         # Aquí deberías guardar el token en algún lugar asociado al usuario para verificarlo luego
#         return JsonResponse({'message': 'Se ha enviado un código de acceso a tu correo electrónico.'})
#     else:
#         return JsonResponse({'error': 'Método no permitido'}, status=405)