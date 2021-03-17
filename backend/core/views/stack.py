from rest_framework import viewsets

from backend.core.models import Stack
from backend.core.serializers import StackSerializer


class StackViewSet(viewsets.ModelViewSet):
    queryset = Stack.objects.all()
    serializer_class = StackSerializer
