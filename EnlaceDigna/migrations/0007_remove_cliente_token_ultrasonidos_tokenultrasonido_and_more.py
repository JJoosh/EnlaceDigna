# Generated by Django 5.0.3 on 2024-04-02 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EnlaceDigna', '0006_alter_doctor_contraseña'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='Token',
        ),
        migrations.AddField(
            model_name='ultrasonidos',
            name='tokenUltrasonido',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='Contraseña',
            field=models.CharField(default='pbkdf2_sha256$720000$T9rVW6mVSLvXnTfbT6ZtN0$UB8z3DdB6ihMBjYIoPkvMpfFeGvaPnbrtETG3aIBjaQ=', max_length=128),
        ),
    ]
