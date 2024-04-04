from django.urls import path


from .api.views import UltrasonidoUploadAPIView

from .api.views import UltrasonidoUploadAPIView  # Adjust the import according to your project structure
from .api.views import  receive_messages, get_galeria

urlpatterns = [
    path('', UltrasonidoUploadAPIView.as_view(), name='upload'),
    
    path('receive_messagess/', receive_messages, name='recibir token'),
    path('get_gallery/<str:token>/', get_galeria, name='Datos galeria'), #URL DE API
  
]
