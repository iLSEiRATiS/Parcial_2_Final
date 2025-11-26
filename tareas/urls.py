from django.urls import path

from . import views

urlpatterns = [
    path("tareas/", views.lista_tareas, name="lista_tareas"),
    path("tareas/crear/", views.crear_tarea, name="crear_tarea"),
    path("tareas/<int:pk>/editar/", views.editar_tarea, name="editar_tarea"),
    path("tareas/<int:pk>/borrar/", views.borrar_tarea, name="borrar_tarea"),
]
