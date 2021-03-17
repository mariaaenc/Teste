from rest_framework import serializers
from backend.core.models import Stack


class StackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stack
        fields = ["id", "name"]
