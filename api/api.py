from .models import Usuario, Objetivo, EmpresaObjetivos, Comprador
from rest_framework import viewsets, permissions
from .serializer import UsuarioSerializer, ObjetivoSerializer, EmpresaObjetivosSerializer, CompradorSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    permission_classes = [permissions.AllowAny]  # O ajusta los permisos según sea necesario
    serializer_class = UsuarioSerializer

class ObjetivoViewSet(viewsets.ModelViewSet):
    queryset = Objetivo.objects.all()
    permission_classes = [permissions.AllowAny]  # O ajusta los permisos según sea necesario
    serializer_class = ObjetivoSerializer

class EmpresaObjetivosViewSet(viewsets.ModelViewSet):
    queryset = EmpresaObjetivos.objects.all()
    permission_classes = [permissions.AllowAny]  # O ajusta los permisos según sea necesario
    serializer_class = EmpresaObjetivosSerializer

class CompradorViewSet(viewsets.ModelViewSet):
    queryset = Comprador.objects.all()
    permission_classes = [permissions.AllowAny]  # O ajusta los permisos según sea necesario
    serializer_class = CompradorSerializer
