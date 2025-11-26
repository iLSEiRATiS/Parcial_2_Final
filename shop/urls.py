from django.urls import path

from . import views

urlpatterns = [
    path("productos/", views.productos_view, name="productos"),
    path("productos/crear/", views.crear_producto, name="crear_producto"),
    path("carrito/", views.carrito_view, name="carrito"),
    path("carrito/agregar/<int:pk>/", views.agregar_carrito, name="agregar_carrito"),
    path("carrito/quitar/<int:pk>/", views.quitar_carrito, name="quitar_carrito"),
]
