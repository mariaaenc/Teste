from django.db import models
from cpffield import cpffield
from .stack import Stack
from datetime import datetime


class Person(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    cpf = cpffield.CPFField("CPF", max_length=14)
    date_birth = models.DateField()
    stack = models.ForeignKey(Stack, on_delete=models.PROTECT, related_name="stacks")
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateField(default=datetime.now)
    deleted_at = models.DateField(default=datetime.now)
