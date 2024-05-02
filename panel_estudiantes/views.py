from django.shortcuts import render

# Create your views here.
def ListadoDeAlumnos(request):
    return render(request, 'listado_alumnos.html')