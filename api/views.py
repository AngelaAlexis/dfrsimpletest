from django.shortcuts import render
from rest_framework import viewsets
from .serializer import UsuarioSerializer, ObjetivoSerializer, EmpresaObjetivosSerializer, CompradorSerializer
from .models import Usuario, Objetivo, EmpresaObjetivos, Comprador

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class ObjetivoViewSet(viewsets.ModelViewSet):
    queryset = Objetivo.objects.all()
    serializer_class = ObjetivoSerializer

class EmpresaObjetivosViewSet(viewsets.ModelViewSet):
    queryset = EmpresaObjetivos.objects.all()
    serializer_class = EmpresaObjetivosSerializer

class CompradorViewSet(viewsets.ModelViewSet):
    queryset = Comprador.objects.all()
    serializer_class = CompradorSerializer
