# Generated by Django 5.0.4 on 2024-04-18 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='Rol',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
