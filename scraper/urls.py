from django.urls import path

from . import views

urlpatterns = [
    path("scraper/buscar/", views.buscar, name="buscar"),
]
