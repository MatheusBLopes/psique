from django.db import models
from django.db.models.fields import CharField
from django.contrib.auth.models import AbstractUser
from rest_framework.permissions import IsAuthenticated


class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Psycologist(models.Model):
    permission_classes = [IsAuthenticated]
    crm = CharField(max_length=200, default="")
    phone = CharField(max_length=200, default="")
    address = CharField(max_length=200, default="")
    cpf = CharField(max_length=200, default="")
    rg = CharField(max_length=200, default="")
    birth_date = CharField(max_length=200, default="")
    category = CharField(max_length=200, default="")
