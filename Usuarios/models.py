from django.db import models

# Create your models here.
class Admin(models.Model):
    Username = models.CharField(max_length=20)
    Password = models.CharField(max_length=20)
    Rol = models.CharField(max_length=10 , null=True, blank=True)

