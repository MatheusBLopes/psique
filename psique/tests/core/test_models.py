from tests.core.factories import PsycologistFactory
import pytest

from  apps.core.models import Psycologist

pytestmark = pytest.mark.django_db

class TestPsycologist:

    def test_psycologist(self, psycologist_object):
        pass
        # psycologist = Psycologist.objects.create(
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

        # assert psycologist.name == "Matheus B. Lopes"
        # assert psycologist.crm == "111.1111.111.11"
        # assert psycologist.email == "matheus.bachiste@teste.com"
        # assert psycologist.phone == "41999999999"
        # assert psycologist.address == "Rua das dores - SP - 83324555"
        # assert psycologist.cpf == "11122233344"
        # assert psycologist.rg == "123456789"
        # assert psycologist.birth_date == "27/06/1998"
        # assert psycologist.password == "123456"