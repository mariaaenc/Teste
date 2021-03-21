from rest_framework.routers import DefaultRouter
from backend.core import views

router = DefaultRouter()

router.register(r"persons", views.PersonViewSet, basename="person")
router.register(r"stacks", views.StackViewSet, basename="stack")
router.register(r"stacksPersons", views.StackPersonViewSet, basename="stacksPerson")
