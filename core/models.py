from django.db import models
from django.db.models.fields import CharField


class Psycologist(models.Model):
    name = CharField(max_length=200, default="")
    crm = CharField(max_length=200, default="")
    email = CharField(max_length=200, default="")
    phone = CharField(max_length=200, default="")
    address = CharField(max_length=200, default="")
    cpf = CharField(max_length=200, default="")
    rg = CharField(max_length=200, default="")
    birth_date = CharField(max_length=200, default="")
    password = CharField(max_length=200, default="")
