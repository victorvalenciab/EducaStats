from django.shortcuts import render, redirect
from .forms import Matricular
from .models import RegisterEstudent


# Create your views here.
title_Matricula = 'Matricula'
title_Listado = 'Alumnos'
h1 = 'EduaStats'
texto = 'Matricula un nuevo alumno'

def ListadoDeAlumnos(request):
    estudiantes_por_grado = {}
    for choice in RegisterEstudent.GRADO_CHOICES:
        if choice[0] != '':
            estudiantes_por_grado[choice[1]] = RegisterEstudent.objects.filter(GradoAcademico=choice[0])    
    return render(request, 'lisEstudiantes.html',{
        'title_Alumnos': title_Listado,
        'estudiantes_por_grado': estudiantes_por_grado
    })

def MatricularAlumno(request):
    alumnos = RegisterEstudent.objects.all()
    if request.method == 'POST':
        form = Matricular(request.POST)
        if form.is_valid():
            # Guardar los datos del formulario en la base de datos
            datos_formulario = form.cleaned_data
            nuevo_estudiante = RegisterEstudent(
                Id=datos_formulario['Id'],
                PrimerNombre=datos_formulario['PrimerNombre'],
                SegundoNombre=datos_formulario['SegundoNombre'],
                PrimerApellido=datos_formulario['PrimerApellido'],
                SegudnoApellido=datos_formulario['SegudnoApellido'],
                Sexo=datos_formulario['Sexo'],
                FechaNacimiento=datos_formulario['FechaNacimiento'],
                Edad=datos_formulario['Edad'],
                Direccion=datos_formulario['Direccion'],
                Telefono=datos_formulario['Telefono'],
                Correo=datos_formulario['Correo'],
                GradoAcademico=datos_formulario['GradoAcademico']
            )
            nuevo_estudiante.save()
            # Redirigir a una página de éxito o a donde desees
            return redirect('MatricularAlumno')
    else:
        form = Matricular()
    return render(request, 'newestudiante.html',{
        'title_Matricula': title_Matricula,
        'h1': h1,
        'texto': texto,
        'form_matricula': form,
        'alumnos': alumnos
    })

def lista_estudiantes(request):
    estudiantes_por_grado = {}
    for choice in RegisterEstudent.GRADO_CHOICES:
        estudiantes_por_grado[choice[0]] = RegisterEstudent.objects.filter(GradoAcademico=1)
    print(estudiantes_por_grado)
    return render(request, 'lisEstudiantes.html', {'estudiantes_por_grado': estudiantes_por_grado})