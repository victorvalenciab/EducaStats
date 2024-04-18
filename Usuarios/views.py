from django.shortcuts import render
from .forms import _Login, _Register, _RestorePassword, _PasswordChanged

# Create your views here.
title = 'EducaStats'
def Login(request):
    title_login = 'Inicair sesión'
    return render(request, 'login.html',{
        'title': title,
        'title_login': title_login,
        'form_login': _Login
    })
    
def Create(request):
    title_crear = 'Crear cuenta'
    return render(request, 'register.html',{
        'title': title,
        'title_crear': title_crear,
        'form_register': _Register
    })
    
def RestorePassword(request):
    title_restore = 'Restablecer contraseña'
    return render(request,'resPassword.html',{
        'title': title,
        'title_restore': title_restore,
        'from_restore': _RestorePassword
    })

def PasswordChanged(request):
    title_changed = 'Restablecer contraseña'
    return render(request, 'passwordChanged.html',{
        'title': title,
        'title_changed': title_changed,
        'form_changed': _PasswordChanged
    })