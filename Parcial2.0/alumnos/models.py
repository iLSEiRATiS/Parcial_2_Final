from django.conf import settings
from django.db import models


class Alumno(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    carrera = models.CharField(max_length=200)
    legajo = models.CharField(max_length=50)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
