from django.urls import path
from .api.views import UltrasonidoUploadAPIView  # Adjust the import according to your project structure
from .api.views import enviar_verificacion, recibir_tokenWhats
urlpatterns = [
    path('upload/', UltrasonidoUploadAPIView.as_view(), name='upload'),
    path('enviar_whats/<str:token>/', enviar_verificacion, name='enviar_mensaje'),
    path('recibir_token/', recibir_tokenWhats, name='recibir token')
]
