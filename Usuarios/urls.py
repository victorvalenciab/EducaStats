from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.Login, name='login'),
    path('register/', views.Create, name='register'),
    path('restorePassword/', views.RestorePassword, name='restorePassword'),
    path('passwordChanged/', views.PasswordChanged, name='passwordChanged'),
]