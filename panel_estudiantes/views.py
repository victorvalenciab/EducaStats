from django.shortcuts import render

# Create your views here.
def ListadoDeAlumnos(request):
    return render(request, 'lisEstudiantes.html')

def MatricularAlumno(request):
    return render(request,'newestudiante.html')
