from django.conf import settings
from django.db import models


class Evento(models.Model):
    CATEGORIAS = [
        ("parcial", "Parcial"),
        ("presentacion", "Presentación"),
        ("otro", "Otro"),
    ]
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    fecha = models.DateField()
    descripcion = models.TextField(blank=True)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default="otro")
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["fecha", "titulo"]

    def __str__(self):
        return f"{self.titulo} - {self.fecha}"
