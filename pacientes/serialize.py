from rest_framework import serializers
from .models import pacientes
class pacientes_seriazer(serializers.ModelSerializer):
    class Meta:
        model=pacientes
        fields='__all__'