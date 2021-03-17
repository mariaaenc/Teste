from django.db import models
from .person import Person


class Stack(models.Model):
    name = models.CharField(max_length=255)
    Person = models.ForeignKey(
        Person, on_delete=models.PROTECT, related_name="persons", default=None
    )
