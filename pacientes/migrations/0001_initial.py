# Generated by Django 5.0.3 on 2024-03-28 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pacientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=100)),
                ('apellido_p', models.CharField(max_length=100)),
                ('apellido_m', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
    ]
