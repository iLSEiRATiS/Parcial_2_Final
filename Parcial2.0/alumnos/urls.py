from django.urls import path

from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("alumnos/", views.lista_alumnos, name="alumnos"),
    path("alumnos/crear/", views.crear_alumno, name="crear_alumno"),
    path("alumnos/<int:pk>/", views.detalle_alumno, name="detalle_alumno"),
    path("alumnos/<int:pk>/editar/", views.editar_alumno, name="editar_alumno"),
    path("alumnos/<int:pk>/eliminar/", views.eliminar_alumno, name="eliminar_alumno"),
    path("alumnos/<int:pk>/enviar_pdf/", views.enviar_pdf, name="enviar_pdf"),
]
