from rest_framework import serializers
from .models import Ultrasonidos
class datos_seriazer(serializers.ModelSerializer):
    class Meta:
        model=Ultrasonidos
        fields='__all__'