from django.shortcuts import render, redirect
from .forms import _Login, _Register, _RestorePassword, _PasswordChanged
from django.db import transaction
from .models import Usuarios

# Create your views here.
title = 'EducaStats'
def Login(request):
    title_login = 'Inicair sesión'
    return render(request, 'login.html',{
        'title': title,
        'title_login': title_login,
        'form_login': _Login
    })
    

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