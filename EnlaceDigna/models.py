from django.db import models

class Doctores(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

class Usuarios(models.Model):
    id=models.AutoField(primary_key=True)
    apellido_p=models.CharField(max_length=50)
    apellido_m=models.CharField(max_length=50)
    correo=models.CharField(max_length=70)
    numero_telefono=models.CharField(max_length=12)

class Ultrasonidos(models.Model):
    id = models.AutoField(primary_key=True)
    ruta_files=models.CharField(max_length=100)
    id_usuario=models.ForeignKey('Usuarios', to_field='id', on_delete=models.CASCADE)
    tipo_ultrasonido=models.CharField(max_length=100)
    fecha=models.DateField()