from django.urls import path
from .api.views import UltrasonidoUploadAPIView
from . import views  # Adjust the import according to your project structure

urlpatterns = [
    path('upload/', UltrasonidoUploadAPIView.as_view(), name='upload'),
    path('registrar/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),



]
