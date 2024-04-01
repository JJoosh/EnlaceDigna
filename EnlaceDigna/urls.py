from django.urls import path
from .api.views import UltrasonidoUploadAPIView  # Adjust the import according to your project structure
from .api.views import enviar_verificacion, recibir_tokenWhats, get_galeria
from . import views 

urlpatterns = [
    path('upload/', UltrasonidoUploadAPIView.as_view(), name='upload'), #URL DE API
    path('registrar/', views.register, name='register'), #URL DE WEB
    path('dashboard/', views.dashboard, name='dashboard'), #URL DE WEB
    path('enviar_whats/<str:cliente_id>/', enviar_verificacion, name='enviar_mensaje'), #URL DE API
    path('recibir_token/', recibir_tokenWhats, name='recibir token'), #URL DE API
    path('get_galeria/<str:token>/', get_galeria, name='Datos galeria'), #URL DE API
    path('galeria/', views.galeria, name='Galeria Usuario' ),

]
