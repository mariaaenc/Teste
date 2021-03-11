from django.db import models
from cpffield import cpffield


class Person(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    cpf = cpffield.CPFField("CPF", max_length=14)
    date_birth = models.DateField()
