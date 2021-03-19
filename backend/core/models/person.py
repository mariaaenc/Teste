from django.db import models
from django.db.models import CharField
from cpffield import cpffield
from datetime import datetime
from django_mysql.models import ListCharField


class Person(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    stacks = ListCharField(
        base_field=CharField(max_length=10),
        size=6,
        max_length=(6 * 11),
        default=None,
        null=True,
    )
    cpf = cpffield.CPFField("CPF", max_length=14)
    date_birth = models.DateField()
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
    deleted_at = models.DateTimeField(default=datetime.now)
