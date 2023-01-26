from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Reparacion(models.Model):

    nombre=models.CharField(max_length=40)
    camada = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Camada {self.camada}"

class Proveedor(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()

class Cliente(models.Model):
    codigo = models.CharField(primary_key=True,max_length=6) 
    nombre= models.CharField(max_length=30)    #nombre
    apellido= models.CharField(max_length=30)    
    telefono= models.CharField(max_length=30)           #apellido
    email= models.EmailField()              
    direccion= models.CharField(max_length=30)          #profesion
    observaciones = models.CharField(max_length=140)

    def __str__(self):
        return f"Codigo: {self.codigo} - Nombre: {self.nombre} - Apellido {self.apellido} - Telefono {self.telefono} - E-Mail {self.email} - Direccion {self.direccion} - Observaciones {self.observaciones}"

class Repuesto(models.Model):
    nombre= models.CharField(max_length=30)
    fechaDeEntrega = models.DateField()  
    entregado = models.BooleanField()

# Clase 24
class Avatar(models.Model):
    
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

    def __str__(self):
        return f"{self.user} - {self.imagen}"