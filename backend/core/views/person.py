from rest_framework import viewsets

from backend.core.models import Person
from backend.core.serializers import PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
