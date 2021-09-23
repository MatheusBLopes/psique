from django.contrib.auth.models import Group, User
from django.db.models import fields
from rest_framework import serializers

from core.models import Psycologist


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class PsycologistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Psycologist
        fields = ['id', 'name', 'crm', 'email', 'phone', 'address', 'cpf', 'rg', 'birth_date', 'password']
