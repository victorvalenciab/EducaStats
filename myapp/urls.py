from django.urls import path
from. import views

urlpatterns = [
    path('Index/', views.MYAPP, name='index'),
    
]