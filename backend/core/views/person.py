from rest_framework import viewsets

from backend.core.models import Person, StackPerson
from backend.core.serializers import PersonSerializer, StackPersonSerializer


class StackPersonViewSet(viewsets.ModelViewSet):
    queryset = StackPerson.objects.all()
    serializer_class = StackPersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
