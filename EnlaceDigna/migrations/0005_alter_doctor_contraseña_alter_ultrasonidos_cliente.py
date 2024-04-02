# Generated by Django 5.0.3 on 2024-04-02 01:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EnlaceDigna', '0004_usuarios_is_authenticated_alter_doctor_contraseña'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='Contraseña',
            field=models.CharField(default='pbkdf2_sha256$720000$MvjmZ10g0Le5sp4pZDyFkl$AnmY5wZkeamAepFvUUDqO9ZxhFanIfEYONvvnoW9OS4=', max_length=128),
        ),
        migrations.AlterField(
            model_name='ultrasonidos',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='EnlaceDigna.cliente'),
        ),
    ]
