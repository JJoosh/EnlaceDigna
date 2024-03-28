from rest_framework import viewsets
from .models import pacientes
from .serialize import pacientes_seriazer

class PacienteViewset(viewsets.ModelViewSet):
    queryset=pacientes.objects.all()
    serializer_class=pacientes_seriazer