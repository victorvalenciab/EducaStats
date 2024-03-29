from django.shortcuts import render

# Create your views here.
def Index(request):
    title = 'EducaStats'
    return render(request, 'index.html',{
        'title': title,
    })