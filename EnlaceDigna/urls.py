from django.urls import path,include
from .api.views import UltrasonidoUploadAPIView  # Adjust the import according to your project structure
from .api.views import enviar_verificacion, recibir_tokenWhats, get_galeria
from . import views 
from rest_framework import routers
from .viewsets import usuarios_viewset

from rest_framework import routers
router = routers.SimpleRouter()
router.register('clientes', usuarios_viewset)

urlpatterns = [

    path('upload/', UltrasonidoUploadAPIView.as_view(), name='upload'),
    path('registrar/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('enviar_whats/<str:cliente_id>/', enviar_verificacion, name='enviar_mensaje'),
    path('recibir_token/', recibir_tokenWhats, name='recibir token'),
    path('get_galeria/<str:token>/', get_galeria, name='Datos galeria'), #URL DE API
    path('galeria/', views.galeria, name='Galeria Usuario' ),
    path('login/', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),
    
]
urlpatterns += router.urls