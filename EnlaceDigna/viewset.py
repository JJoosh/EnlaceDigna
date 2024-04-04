from rest_framework import viewsets
from .models import Ultrasonidos
from .serialize import datos_seriazer

class datos_viewset(viewsets.ModelViewSet):
    queryset=Ultrasonidos.objects.all()
    serializer_class= datos_seriazer