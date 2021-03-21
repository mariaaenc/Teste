from rest_framework import serializers
from backend.core.models import Person
from backend.core.models import StackPerson
from .stackPersons import StacksPersonSerializer, StackPersonSerializer
from django.db import transaction


class PersonSerializer(serializers.ModelSerializer):
    stacks = StacksPersonSerializer(source="persons", many=True, readOnly=True)

    class Meta:
        model = Person
        fields = [
            "id",
            "name",
            "address",
            "email",
            "cpf",
            "date_birth",
            "created_at",
            "updated_at",
            "deleted_at",
            "stacks",
        ]

    @transaction.atomic
    def create(self, validated_data):
        print(validated_data)
        user = validated_data.copy()
        persons = user.pop("persons")  # stacks
        person = Person.objects.update_or_create(
            name=user["name"],
            address=user["address"],
            email=user["email"],
            cpf=user["cpf"],
            date_birth=user["date_birth"],
        )
        print("@@@@@@@@@@@@@@@@@@@")
        print(person)
        for stack in persons:
            stackPerson = StackPersonSerializer.create(
                StackPersonSerializer(),
                validated_data={"stack": stack["stack"], "person": person[0]},
            )
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        return person
