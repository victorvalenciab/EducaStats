from django.urls import path
from . import views

urlpatterns = [
    path('estudiastes/', views.ListadoDeAlumnos, name='ListadoDeAlumnos'),
    path('matricular_alumno/', views.MatricularAlumno, name='MatricularAlumno'),
    path('Alumnos', views.lista_estudiantes, name='lista_estudiantes'),
]