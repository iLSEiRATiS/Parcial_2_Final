from django.urls import path

from . import views

urlpatterns = [
    path("apuntes/", views.lista_apuntes, name="apuntes"),
    path("apuntes/crear/", views.crear_apunte, name="crear_apunte"),
    path("apuntes/<int:pk>/", views.detalle_apunte, name="detalle_apunte"),
    path("apuntes/<int:pk>/editar/", views.editar_apunte, name="editar_apunte"),
]
