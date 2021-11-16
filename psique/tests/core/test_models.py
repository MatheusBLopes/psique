import pytest

# from apps.core.models import Psychologist
# from tests.core.factories import PsychologistFactory

pytestmark = pytest.mark.django_db


class TestPsychologist:
    def test_psychologist(self, psychologist_object):
        pass
        # psychologist = Psychologist.objects.create(
        #     name="Matheus B. Lopes",
        #     crm="111.1111.111.11",
        #     email="matheus.bachiste@teste.com",
        #     phone="41999999999",
        #     address="Rua das dores - SP - 83324555",
        #     cpf="11122233344",
        #     rg="123456789",
        #     birth_date="27/06/1998",
        #     password="123456",
        # )

        # assert psychologist.name == "Matheus B. Lopes"
        # assert psychologist.crm == "111.1111.111.11"
        # assert psychologist.email == "matheus.bachiste@teste.com"
        # assert psychologist.phone == "41999999999"
        # assert psychologist.address == "Rua das dores - SP - 83324555"
        # assert psychologist.cpf == "11122233344"
        # assert psychologist.rg == "123456789"
        # assert psychologist.birth_date == "27/06/1998"
        # assert psychologist.password == "123456"
