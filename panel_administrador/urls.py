from django.urls import path
from . import views

urlpatterns = [
    path('Vic/', views.Index, name='panel_administrador'),  
]