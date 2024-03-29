from django import forms

class _AdminForm(forms.Form):
    Username = forms.CharField(max_length=20)
    Password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    
class _Login(forms.Form):
    Username_Login = forms.CharField(label="Usuario", max_length=20, widget=forms.TextInput(attrs={'class':'forms_Usuario'}))
    Password_Login = forms.CharField(label="Contraseña", max_length=50, widget=forms.PasswordInput(attrs={'class':'forms_Password'}))
    SeePassword = forms.BooleanField(label="Ver contraseña", widget=forms.CheckboxInput(attrs={'class':'forms_SeePassword'}))
    
class _Create(forms.Form):
    gmail_Create = forms.EmailField(label="Correo electrónico", max_length=50)
    Name_Create = forms.CharField(label="Nombre completo", max_length=20)
    Password_Create = forms.CharField(label="Contraseña", max_length=50, widget=forms.PasswordInput)
    Password_Confirm = forms.CharField(label="Confirmar contraseña", max_length=20, widget=forms.PasswordInput)

class _RestorePassword(forms.Form):
    gmail_Restore = forms.EmailField(label="Correo electrónico", max_length=50)

class _PasswordChanged(forms.Form):
    NewPassword = forms.CharField(label="Nueva contraseña", max_length=50, widget=forms.PasswordInput)
    RepitNewPassword = forms.CharField(label="Repita la nueva contraseña", max_length=50, widget=forms.PasswordInput)