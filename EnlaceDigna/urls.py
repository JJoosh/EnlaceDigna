from django.urls import path
from .views import dashboard_view
from . import views
from .api.views import UltrasonidoUploadAPIView, enviar_verificacion, recibir_tokenWhats
from rest_framework_simplejwt.views import TokenRefreshView  # Asegúrate de que esto está descomentado y correctamente importado

urlpatterns = [
    path('', UltrasonidoUploadAPIView.as_view(), name='upload'),
    path('registrar/', views.register, name='register'),      
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('enviar_whats/<str:cliente_id>/', enviar_verificacion, name='enviar_mensaje'),
    path('recibir_token/', recibir_tokenWhats, name='recibir_token'),  
    path('login/', views.login_view, name='login'),
    # path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
