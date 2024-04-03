from django.db import models
import random
from django.contrib.auth.hashers import make_password

class Usuarios(models.Model):
    Nombre = models.CharField(max_length=255, null=False)
    Apellido_Paterno = models.CharField(max_length=255, null=False)
    Apellido_Materno = models.CharField(max_length=255, blank=True, null=True)
    Correo = models.EmailField(max_length=255, null=False, unique=True)
    NumeroCelular = models.CharField(max_length=20, blank=True, null=True)
    Rol = models.CharField(max_length=50, null=False)

    

    def __str__(self):
        return f'{self.Nombre} {self.Apellido_Paterno}'

    

class Cliente(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    

class Doctor(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    Contraseña = models.CharField(max_length=128, default=make_password('1234'))
    def __str__(self):
        return self.usuario.Nombre

    def save(self, *args, **kwargs):
        self.Contraseña = make_password(self.Contraseña)
        super().save(*args, **kwargs)

class Ultrasonidos(models.Model):
    ruta_files = models.TextField()
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)    
    TipoDeUltrasonidos = models.CharField(max_length=255, null=False)
    Fecha = models.DateField(auto_now_add=True)
    tokenUltrasonido=models.CharField(max_length=10, null=True)
    
    def __str__(self):
        return f'{self.TipoDeUltrasonidos} - {self.Fecha}'
