# Generated by Django 5.0.3 on 2024-04-01 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EnlaceDigna', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='Contraseña',
            field=models.CharField(default='pbkdf2_sha256$720000$O56PKWeHAGZkQmve7MjHjy$mQNsuPRWvERnWx2wxub7UHZzX7RBScSm0b+Ka2k7cK0=', max_length=128),
        ),
    ]
