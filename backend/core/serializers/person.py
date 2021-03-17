from rest_framework import serializers
from backend.core.models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ["id", "name", "address", "email", "cpf", "date_birth"]


class PersonDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ["id", "name", "address", "email", "cpf", "date_birth", "stack"]

