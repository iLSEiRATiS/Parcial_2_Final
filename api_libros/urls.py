from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import LibroViewSet

router = DefaultRouter()
router.register(r"api/libros", LibroViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
