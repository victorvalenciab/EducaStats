from django import forms
from .models import RegisterEstudent
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

 

OPCIONES_SEXO = [
    ("","Seleccionar"),
    ("Masculino", "Masculino"),
    ("Femenino", "Femenino"),
]
OPCIONES_GRADO = [
    ('','Seleccionar'),
    (0, 'Prescolar'),
    (1, 'Primero'),
    (2, 'Segundo'),
    (3, "Tercero"),
    (4, "Cuarto"),
    (5, "Quinto"),
    (6, "Sexto"),
    (7, "Septimo"),
    (7, "Octavo"),
    (9, "Noveno"),
    (10, "Decimo"),
    (11, "Onceavo"),
]
USUARIO_ROLES = (
    ('','Seleccionar'),
        ('Rector', 'Rector'),
        ('Docente', 'Docente'),
        ('Estudiante', 'Estudiante'),
    )
class Matricular(forms.ModelForm):
    Id = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'forms_Id input'}), required=True)
    PrimerNombre = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'PriemrNombre'}), required=True)
    SegundoNombre = forms.CharField(max_length=200)
    PrimerApellido = forms.CharField(max_length=200, required=True)
    SegudnoApellido = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'SegudnoApellido'}),)
    Sexo = forms.ChoiceField(choices=OPCIONES_SEXO, widget=forms.Select(attrs={'class':'forms_Sexo'}), required=True)
    FechaNacimiento = forms.DateField(required=True)
    Edad = forms.IntegerField(required=True)
    Direccion = forms.CharField(max_length=200, required=True)
    Telefono = forms.IntegerField(required=True)
    Correo = forms.EmailField(required=True)
    GradoAcademico = forms.ChoiceField(choices=OPCIONES_GRADO, widget=forms.Select(attrs={'class':'forms_GradoAcademico'}), required=True)
    Contraseña = forms.CharField(max_length=200, widget=forms.PasswordInput(attrs={'class':'forms_Contraseña'}), required=True)
    rol = forms.ChoiceField(choices=USUARIO_ROLES, required=True)

    class Meta:
        model = User
        fields = ['Correo', 'Contraseña', 'rol']  # Asume que 'username' es el campo de 'Usuario'

    def save(self, commit=True):
        user = super(Matricular, self).save(commit=False)
        user.set_password(self.cleaned_data['Contraseña'])
        if commit:
            user.save()
        return user
    
 
    
class Buscar(forms.Form):
    OPCIONES_GRADO = [
    ('','Seleccionar'),
    (0, 'Prescolar'),
    (1, 'Primero'),
    (2, 'Segundo'),
    (3, "Tercero"),
    (4, "Cuarto"),
    (5, "Quinto"),
    (6, "Sexto"),
    (7, "Septimo"),
    (7, "Octavo"),
    (9, "Noveno"),
    (10, "Decimo"),
    (11, "Onceavo"),
    ]
    Buscar = forms.ChoiceField(choices=OPCIONES_GRADO)