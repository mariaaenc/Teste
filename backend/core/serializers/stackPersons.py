from rest_framework import serializers
from backend.core.models import StackPerson


class StacksPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = StackPerson
        fields = ("stack", "datetime", "stack_name")


class StackPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = StackPerson
        fields = ("person", "stack", "datetime", "stack_name", "person_name")
