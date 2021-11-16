import re
from functools import reduce

from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.db.models import Q
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import Category, Psychologist


class LoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token["email"] = str(user.email)
        return token


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ("username", "password", "password2", "email", "first_name", "last_name")
        extra_kwargs = {"first_name": {"required": True}, "last_name": {"required": True}}

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )

        user.set_password(validated_data["password"])
        user.save()

        return user


class BaseCreatePsychologistSerializer:
    def _is_unique(self, cpf, rg, crp):
        keyword_arguments = []
        if cpf:
            keyword_arguments.append(Q(cpf=cpf))
        if rg:
            keyword_arguments.append(Q(rg=rg))
        if crp:
            keyword_arguments.append(Q(crp=crp))

        keyword_arguments = reduce(lambda a, b: a | b, keyword_arguments)
        return Psychologist.objects.filter(keyword_arguments).exists()

    def _validate_documents(self, cpf, rg, crp):
        if cpf is None or rg is None or crp is None:
            return

    def validate(self, attrs):
        cpf = attrs.get("cpf")
        rg = attrs.get("rg")
        crp = attrs.get("crp")

        self._validate_documents(cpf, rg, crp)

        if self._is_unique(cpf, rg, crp):
            raise serializers.ValidationError(
                {"documents": ("A psychologist with this CRP, CPF, RG or USER already exists.")}
            )

        return attrs


class PsychologistSerializer(BaseCreatePsychologistSerializer, serializers.ModelSerializer):
    class Meta:
        model = Psychologist
        fields = [
            "id",
            "full_name",
            "cpf",
            "rg",
            "crp",
            "birth_date",
            "address",
            "category",
            "whatsapp_phone",
            "about",
            "picture_url",
            "status",
            "paused",
            "blocked",
            "blocked_reason",
            "last_blocked_on",
            "in_an_appointment",
            "registration_approved_by",
        ]

    def create(self, validated_data):
        user_id = self.context["request"].auth["user_id"]

        if Psychologist.objects.filter(user_id=user_id).exists():
            raise serializers.ValidationError({"User": ("A psychologist for this user already exists.")})

        user = User.objects.filter(id=user_id).first()
        validated_data["user_id"] = user
        return Psychologist.objects.create(**validated_data)

    def validate_crp(self, crp):
        return re.sub(r"[^0-9]", "", crp)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]
