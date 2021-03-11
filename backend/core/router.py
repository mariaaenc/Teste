from rest_framework.routers import DefaultRouter
from backend.core import views

router = DefaultRouter()

router.register(r"persons", views.PersonViewSet, basename="person")
