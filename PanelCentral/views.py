from django.shortcuts import render, redirect

# Create your views here.
def panelIndex(request):
    title = 'EducaStats'
    return render(request, 'panelIndex.html',{
        'title': title,
    })
    