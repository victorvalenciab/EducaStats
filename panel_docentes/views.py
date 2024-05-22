from django.shortcuts import render

# Create your views here.

title_Matricula = 'Matricula'
title_Listado = 'Alumnos'
h = 'EduaStats'

def pl_docentes(request):
    return render(request, 'pl_docentes.html')