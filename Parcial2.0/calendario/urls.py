from django.urls import path

from . import views

urlpatterns = [
    path("calendario/", views.lista_eventos, name="eventos"),
    path("calendario/crear/", views.crear_evento, name="crear_evento"),
    path("calendario/<int:pk>/editar/", views.editar_evento, name="editar_evento"),
    path("calendario/<int:pk>/eliminar/", views.eliminar_evento, name="eliminar_evento"),
]
