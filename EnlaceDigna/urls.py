from django.urls import path
from .views import dashboard_view
from . import views
from .api.views import UltrasonidoUploadAPIView, enviar_verificacion, recibir_tokenWhats
from rest_framework_simplejwt.views import TokenRefreshView  # Asegúrate de que esto está descomentado y correctamente importado

from .api.views import UltrasonidoUploadAPIView  # Adjust the import according to your project structure
from .api.views import enviar_verificacion, recibir_tokenWhats, get_galeria
from . import views 

urlpatterns = [
    path('', UltrasonidoUploadAPIView.as_view(), name='upload'),
    
    path('recibir_token/', recibir_tokenWhats, name='recibir token'),
    path('get_galeria/<str:token>/', get_galeria, name='Datos galeria'), #URL DE API
  
]
