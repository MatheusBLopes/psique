import factory

from apps.core.models import Psychologist


class PsychologistFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Psychologist

    name = "Matheus B. Lopes"
    crm = "111.1111.111.11"
    email = "matheus.bachiste@teste.com"
    phone = "41999999999"
    address = "Rua das dores - SP - 83324555"
    cpf = "11122233344"
    rg = "123456789"
    birth_date = "27/06/1998"
    password = "123456"
