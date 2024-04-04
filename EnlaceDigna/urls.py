from django.urls import path


from .api.views import UltrasonidoUploadAPIView

from .api.views import UltrasonidoUploadAPIView  # Adjust the import according to your project structure
from .api.views import  receive_messages, get_galeria


urlpatterns = [
    path('', UltrasonidoUploadAPIView.as_view(), name='upload'),
    
    path('recibir_token/', receive_messagess, name='recibir token'),
    path('get_galeria/<str:token>/', get_galeria, name='Datos galeria'), #URL DE API
  
]

