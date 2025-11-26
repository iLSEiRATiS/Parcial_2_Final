from django.urls import path

from . import views

urlpatterns = [
    path("scraper/", views.scraper_view, name="scraper"),
]
