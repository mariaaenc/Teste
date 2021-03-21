from django.db import models
from cpffield import cpffield
from datetime import datetime


class Person(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    stacks = models.CharField(default=None, null=True, max_length=500)
    cpf = cpffield.CPFField("CPF", max_length=14)
    date_birth = models.DateField()
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
    deleted_at = models.DateTimeField(default=datetime.now)
