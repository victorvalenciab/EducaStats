from django.urls import path
from . import views

urlpatterns = [
    path('panelIndex/', views.panelIndex, name='pollo'),
]