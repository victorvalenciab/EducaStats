from django.http import HttpResponse
from django.shortcuts import render, redirect
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
    
def Register(request):
    title_crear = 'Crear cuenta'
    if request.method == 'GET':
        return render(request, 'register.html',{
        'title': title,
        'title_crear': title_crear,
        'form_register': _Register
        })
# def Register(request):
#     if request.method == 'POST':
#         form = _Register(request.POST)
#         if form.is_valid():
#             # Crea una instancia del modelo con los datos del formulario
#             register = form.save(commit=False)
#             # Realiza cualquier otra lógica adicional si es necesario
#             Register.save()  # Guarda la instancia en la base de datos
#             return redirect('login.html')  # Redirige a la URL de éxito
#     else:
#         form = _Register()
#     return render(request, 'register.html', {'form': form})
    

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