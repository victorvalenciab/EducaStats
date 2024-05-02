from django.shortcuts import render


# Create your views here.
def MYAPP(request):
    return render(request, 'my_app.html')

def my_app_view(request):
    return render(request, 'my_app.html')