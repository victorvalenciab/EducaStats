from django.shortcuts import render

# Create your views here.
def Index(request):
    title = 'EducaStats'
    return render(request, 'panel_Administrador.html',{
        'title': title,
    })
