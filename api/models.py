from django.db import models

# Modelo para Usuarios
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=100)

# Modelo para Objetivos
class Objetivo(models.Model):
    nombre = models.CharField(max_length=100)
    direccion_ip = models.CharField(max_length=100)
    tiempo_realizar = models.FloatField()

# Modelo para EmpresasObjetivos
class EmpresaObjetivos(models.Model):
    nombre_empresa = models.CharField(max_length=100)
    num_trabajadores = models.IntegerField()
    tiempo_realizar = models.FloatField()

# Modelo para Compradores
class Comprador(models.Model):
    nombre = models.CharField(max_length=100)
    num_compras = models.IntegerField()
    total_pagado = models.FloatField()
