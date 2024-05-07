from django.urls import path
from . import views

urlpatterns = [
    path('admistracion/', views.Iadministrador, name='panel_administrador'),  
]