from rest_framework import serializers
from .models import Cadastre


class CadastreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cadastre
        fields = '__all__'
