from django.db import models

# Create your models here.
class pacientes(models.Model):
    Nombre=models.CharField(max_length=100)
    apellido_p=models.CharField(max_length=100)
    apellido_m=models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email=models.CharField(max_length=100)

    def __str__(self):
        return self.Nombre