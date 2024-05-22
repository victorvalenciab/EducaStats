from django.urls import path
from . import views

urlpatterns = [
    path('Docentes/', views.pl_docentes, name='pl_docentes'),
    ]