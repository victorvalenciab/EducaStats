from django.shortcuts import render


# Create your views here.
def MYAPP(request):
    return render(request, 'myapp.html')