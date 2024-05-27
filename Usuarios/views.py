from django.shortcuts import render, redirect
from .forms import _Login, _RestorePassword, _PasswordChanged
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login



# Create your views here.
# def login_view(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']
#         user = authenticate(request, username=email, password=password)

#         if user is not None:
#             login(request, user)
#             # Redirige a una página de éxito.
#             return redirect('nombre_de_tu_pagina_de_exito')# Redirige a la vista de my_app.html
#         else:
#             # Devuelve un mensaje de error 'invalid login'.
#             return render(request, 'login.html', {'error': 'Correo electrónico o contraseña inválidos.'})
#     else:
#         return render(request, 'login.html')

title = 'EducaStats'
def Login(request):
    title_login = 'Iniciar sesión'
    form_login = _Login(request.POST or None)

    if form_login.is_valid():
        email = form_login.cleaned_data.get('Gmail_Login')
        password = form_login.cleaned_data.get('Password_Login')
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            # Redirige a la página 'lisEstudiantes' en la aplicación 'panale_estudiantes'.
            return redirect('panale_estudiantes:lisEstudiantes')
        else:
            # Devuelve un mensaje de error 'invalid login'.
            form_login.add_error(None, 'Correo electrónico o contraseña inválidos.')

    return render(request, 'login.html', {
        'title': title,
        'title_login': title_login,
        'form_login': form_login
    })
 
    
    
def Users(request):
   Username = request.POST['Username']
   Password = request.POST['Username']
   User = Usuarios(Username_Login = Username, Password_Login = Password)
   User.save();
   return redirect('my_app')


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