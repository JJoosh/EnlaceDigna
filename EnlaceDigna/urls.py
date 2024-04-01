from django.urls import path
from .api.views import UltrasonidoUploadAPIView  # Adjust the import according to your project structure
from .api.views import enviar_verificacion, recibir_tokenWhats
from . import views 
urlpatterns = [
    path('upload/', UltrasonidoUploadAPIView.as_view(), name='upload'),
    path('registrar/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('enviar_whats/<str:cliente_id>/', enviar_verificacion, name='enviar_mensaje'),
    path('recibir_token/', recibir_tokenWhats, name='recibir token'),
    path('login/', views.login_view, name='login'),
]
