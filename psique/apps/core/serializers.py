from django.contrib.auth.models import Group
from django.db.models import fields
from rest_framework import serializers

from .models import Psycologist

from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']


class PsycologistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Psycologist
        fields = ['id', 'name', 'crm', 'email', 'phone', 'address', 'cpf', 'rg', 'birth_date', 'password', 'category']
