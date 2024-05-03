from django.db import models

# Create your models here.
SEXO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )
GRADO_CHOICES = (
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
)

class RegisterEstudent(models.Model):
    Id = models.IntegerField(primary_key=True)
    PrimerNombre = models.CharField(max_length=200)
    SegundoNombre = models.CharField(max_length=200)
    PrimerApellido = models.CharField(max_length=200)
    SegudnoApellido = models.CharField(max_length=200)
    Sexo = models.CharField(max_length=1,choices=SEXO_CHOICES)
    FechaNacimiento = models.DateField()
    Edad = models.IntegerField(null=True, blank=True)
    Direccion = models.CharField(max_length=200)
    Telefono = models.IntegerField()
    Correo = models.EmailField()
    GradoAcademico = models.IntegerField(choices=GRADO_CHOICES)

    def __str__(self):
        return self. PrimerNombre