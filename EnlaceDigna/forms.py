from django import forms

class RegisterForm(forms.Form):
    name = forms.CharField(label='Nombre', max_length=100)
    apellido_paterno = forms.CharField(label='Apellido Paterno', max_length=100)
    apellido_materno = forms.CharField(label='Apellido Materno', max_length=100)
    number = forms.CharField(label='Numero telefonico', max_length=20)
    email = forms.EmailField(label='Correo electronico')
    # If paciente choices are static, define them here, or fetch from a model
    paciente_choices = [('paciente', 'Paciente')]  # Example: [('value1', 'Choice 1'), ('value2', 'Choice 2')]
    rol = forms.ChoiceField(label='Paciente', choices=paciente_choices)
