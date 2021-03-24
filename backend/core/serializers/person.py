from rest_framework import serializers
from backend.core.models import Person, StackPerson
from .stackPersons import StacksPersonSerializer
from django.db import transaction


class PersonSerializer(serializers.ModelSerializer):
    stacks = StacksPersonSerializer(source="persons", many=True)

    class Meta:
        depth = 1
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
        person = validated_data.copy()
        try:
            stacks = person.pop("persons")  # stacks
        except:
            stacks = []
        person = Person(
            name=person["name"],
            address=person["address"],
            email=person["email"],
            cpf=person["cpf"],
            date_birth=person["date_birth"],
        )
        person.save()
        for stack in stacks:
            print(stack)
            stackPerson = StackPerson(stack=stack["stack"], person=person)
            stackPerson.save()
        return person

    def update(self, instance, validated_data):
        stacks = validated_data.pop("persons")  # stacks
        instance.name = validated_data.get("name", instance.name)
        instance.address = validated_data.get("address", instance.address)
        instance.email = validated_data.get("email", instance.email)
        instance.cpf = validated_data.get("cpf", instance.cpf)
        instance.date_birth = validated_data.get("date_birth", instance.date_birth)
        instance.updated_at = validated_data.get("updated_at", instance.updated_at)
        # instance.deleted_at = validated_data.get("deleted_at", instance.deleted_at)
        instance.save()

        fixedStacks = []
        allStacksPerson = StackPerson.objects.filter(person=instance.id)

        for stack in stacks:
            # print(stack["stack"].id)
            if StackPerson.objects.filter(
                person=instance.id, stack=stack["stack"].id
            ).exists():
                fixedStacks.append(stack["stack"].id)
            else:
                newStackPerson = StackPerson.objects.create(
                    stack=stack["stack"], person=instance
                )
                newStackPerson.save()
                fixedStacks.append(newStackPerson.stack.id)

        print("******stacks a serem fixadas*******")
        print(fixedStacks)
        for i in allStacksPerson:
            allStacksPersonID = i.stack.id
            print("******todas as stacks desse usuário*******")
            print(allStacksPersonID)
            if allStacksPersonID not in fixedStacks:
                print("******relações a serem deletadas*******")
                print(allStacksPersonID)
                i.delete()
        return instance
