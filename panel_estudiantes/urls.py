from django.urls import path
from . import views

urlpatterns = [
    path('estudiastes/', views.ListadoDeAlumnos, name='ListadoDeAlumnos'),
    path('matricular_alumno/', views.MatricularAlumno, name='MatricularAlumno'),
    path('pl_alumnos/', views.pl_alumnos, name='pl_alumnos'),
    ]