from rest_framework import serializers
from .models import Usuario, Objetivo, EmpresaObjetivos, Comprador

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class ObjetivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Objetivo
        fields = '__all__'

class EmpresaObjetivosSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpresaObjetivos
        fields = '__all__'

class CompradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comprador
        fields = '__all__'
