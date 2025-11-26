from django.urls import path

from . import views

urlpatterns = [
    path("informes/", views.informes_view, name="informes"),
    path("reporte/<int:pk>/pdf/", views.reporte_pdf, name="reporte_pdf"),
]
