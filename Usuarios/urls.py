from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.Login, name='login'),
    path('Users/', views.Users, name='Users'),
    path('restorePassword/', views.RestorePassword, name='restorePassword'),
    path('passwordChanged/', views.PasswordChanged, name='passwordChanged'),
]