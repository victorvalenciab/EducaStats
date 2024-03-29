from django.shortcuts import render
from .forms import _Login, _Create

# Create your views here.
list = 'EducaStats'
def Login(request):
    return render(request, 'login.html',{
        'title': list,
        'form_login': _Login
    })
    
def Create(request):
    return render(request, 'createAc.html',{
        'title': list,
        'form_create': _Create
    })