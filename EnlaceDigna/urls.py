from django.urls import path
<<<<<<< HEAD
from .views import dashboard_view
from . import views
from .api.views import UltrasonidoUploadAPIView, enviar_verificacion, recibir_tokenWhats
from rest_framework_simplejwt.views import TokenRefreshView  # Asegúrate de que esto está descomentado y correctamente importado
=======
from .api.views import UltrasonidoUploadAPIView  # Adjust the import according to your project structure
from .api.views import enviar_verificacion, recibir_tokenWhats, get_galeria
from . import views 
>>>>>>> 4aec583b7a77517d3bf1890cd22d4580abbacbf1

urlpatterns = [
    path('', UltrasonidoUploadAPIView.as_view(), name='upload'),
    path('registrar/', views.register, name='register'),      
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('enviar_whats/<str:cliente_id>/', enviar_verificacion, name='enviar_mensaje'),
<<<<<<< HEAD
    path('recibir_token/', recibir_tokenWhats, name='recibir_token'),  
    path('login/', views.login_view, name='login'),
    # path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
=======
    path('recibir_token/', recibir_tokenWhats, name='recibir token'),
    path('get_galeria/<str:token>/', get_galeria, name='Datos galeria'), #URL DE API
    path('galeria/', views.galeria, name='Galeria Usuario' ),
    path('login/', views.login_view, name='login'),

>>>>>>> 4aec583b7a77517d3bf1890cd22d4580abbacbf1
]
