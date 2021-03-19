from rest_framework import serializers
from backend.core.models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = [
            "id",
            "name",
            "address",
            "email",
            "cpf",
            "stacks",
            "date_birth",
            "created_at",
            "updated_at",
            "deleted_at",
        ]
