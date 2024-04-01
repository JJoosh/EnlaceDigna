from rest_framework import viewsets
from .models import Usuarios
from .serialize import usuarios_seriazer

class usuarios_viewset(viewsets.ModelViewSet):
    queryset=Usuarios.objects.all()
    serializer_class=usuarios_seriazer