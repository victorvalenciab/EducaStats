from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
title = 'EducaStats'
h1 = 'EducaStats'

def MYAPP(request):
    return render(request, 'my_app.html', {
        'title': title,
        'h1': h1
    })

# def my_app_view(request):
#     return render(request, 'my_app.html')