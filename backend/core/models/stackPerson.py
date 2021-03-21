from django.db import models
from datetime import datetime
from .person import Person
from .stack import Stack


class StackPerson(models.Model):
    stack = models.ForeignKey(Stack, on_delete=models.CASCADE, related_name="stacks")
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="persons")
    datetime = models.DateField(default=datetime.now())

    class Meta:
        unique_together = [["stack", "person"]]

    @property
    def stack_name(self):
        return self.stack.name

    @property
    def person_name(self):
        return self.person.name

