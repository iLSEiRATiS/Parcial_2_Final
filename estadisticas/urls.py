from django.urls import path

from . import views

urlpatterns = [
    path("estadisticas/dashboard/", views.dashboard, name="dashboard"),
]
