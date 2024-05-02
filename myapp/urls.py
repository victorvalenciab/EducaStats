from django.urls import path
from. import views

urlpatterns = [
    path('my_app/', views.MYAPP, name='my_app'),     
]