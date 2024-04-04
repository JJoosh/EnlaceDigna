from django.urls import path


from .api.views import UltrasonidoUploadAPIView, recibir_tokenWhats

from .api.views import UltrasonidoUploadAPIView  # Adjust the import according to your project structure
from .api.views import  recibir_tokenWhats, get_galeria
from rest_framework import routers
from .viewset import datos_viewset



urlpatterns = [
    path('', UltrasonidoUploadAPIView.as_view(), name='upload'),
    path('recibir_token/', recibir_tokenWhats, name='recibir token'),
    path('get_galeria/<int:id>/', get_galeria, name='Datos galeria'), #URL DE API
]

