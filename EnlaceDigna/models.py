from django.db import models
import random


class Usuarios(models.Model):
    Nombre = models.CharField(max_length=255, null=False)
    Apellido_Paterno = models.CharField(max_length=255, null=False)
    Apellido_Materno = models.CharField(max_length=255, blank=True, null=True)
    Correo = models.EmailField(max_length=255, null=False, unique=True)
    NumeroCelular = models.CharField(max_length=20, blank=True, null=True)
    Rol = models.CharField(max_length=50, null=False)

    def __str__(self):
        return f'{self.Nombre} {self.Apellido_Paterno}'

    def save(self, *args, **kwargs):
        is_new = not self.pk  # Determina si el objeto es nuevo
        super(Usuarios, self).save(*args, **kwargs)  # Guarda el objeto Usuario primero
        
        if is_new and self.Rol.lower() == 'paciente':
            # Combina las 2 primeras letras del nombre y apellido con un número aleatorio de 4 dígitos
            token_prefix = self.Nombre[:2].lower() + self.Apellido_Paterno[:2].lower()
            token_number = str(random.randint(1000, 9999))
            token = token_prefix + token_number
            Cliente.objects.create(usuario=self, Token=token)  # Crea un nuevo Cliente relacionado

class Cliente(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    Token = models.CharField(max_length=255, null=False)
    def __str__(self):
        return self.Token
class Doctor(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    def __str__(self):
        return self.usuario.Nombre

class Ultrasonido(models.Model):
    ruta_files = models.TextField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    TipoDeUltrasonidos = models.CharField(max_length=255, null=False)
    Fecha = models.DateField(auto_now_add=True)
    def __str__(self):
        return f'{self.TipoDeUltrasonidos} - {self.Fecha}'
