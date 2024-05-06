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

@login_required
def Login(request):
    title = 'EducaStats'
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
 
    
    
# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('my_app.html')  # Redirige a la vista de my_app.html
#         else:
#             # Manejar el error de autenticación
#             return render(request, 'login.html', {'error': 'Credenciales inválidas'})
#     else:
#         return render(request, 'login.html')
    
def Users(request):
   Username = request.POST['Username']
   Password = request.POST['Username']
   User = Usuarios(Username_Login = Username, Password_Login = Password)
   User.save();
   return redirect('my_app')

# @transaction.atomic
# def Register(request): 
#     title_crear = 'Crear cuenta'
#     if request.method == 'POST':
#         newUSer = _Register(request.POST)
#         if newUSer.is_valid():
#             Email = newUSer.cleaned_data['gmail_Register']
#             Username = newUSer.cleaned_data['Name_Register']
#             Rol = newUSer.cleaned_data['Rol_Register']
#             Password = newUSer.cleaned_data['Password_Register']
#             PasswordChange = newUSer.cleaned_data['Password_RegisterConfirm']
#             # Realiza aquí tus operaciones de escritura en la base de datos
#             # Por ejemplo:
#             nuevo_usuario = _Register(email=Email, username=Username, rol=Rol, password=Password, passwordChange=PasswordChange)
#             nuevo_usuario.save()
#             return redirect('login')
#     else:
#         newUSer = _Register()
#     return render(request, 'register.html', {
#         'newUSer': newUSer,
#         'title': title,
#         'title_crear': title_crear,
#     })


# def registerUser(request):
#     gmail_Register= request.POST['gmail_Register']
#     Name_Register= request.POST['Name_Register']
#     Rol_Register= request.POST['Rol_Register']
#     Password_Register= request.POST['Password_Register']
#     Password_RegisterConfirm= request.POST['Password_RegisterConfirm']

#     register = _Register(
#         Email= gmail_Register,
#         Username= Name_Register,
#         Rol= Rol_Register,
#         Password= Password_Register,
#         PasswordChange= Password_RegisterConfirm
#     )
#     register.save()
#     return redirect('/')
        

    

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