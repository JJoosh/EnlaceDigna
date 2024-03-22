from django.urls import path
from .api.views import UltrasonidoUploadAPIView  # Adjust the import according to your project structure

urlpatterns = [
    path('upload/', UltrasonidoUploadAPIView.as_view(), name='upload'),
]
