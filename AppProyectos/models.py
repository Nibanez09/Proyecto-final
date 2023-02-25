from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    empresa = models.CharField(max_length=40)
    profesion = models.CharField(max_length=40)
    email = models.EmailField()

class Proyecto(models.Model):
    codigo = models.CharField(max_length=40)
    fecha_recibido = models.DateField()
    plazo = models.IntegerField()
    categoria = models.CharField(max_length=40)
    imagen = models.ImageField(upload_to="proyectos", null=True, blank=True)

class Responsable(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)

class AvatarImagen(models.Model):
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)
