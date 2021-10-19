# import json
# from unittest import mock

import pytest

# from rest_framework import status
# from rest_framework.test import APIClient


from .core.factories import PsycologistFactory

@pytest.fixture
def psycologist_object():
    return PsycologistFactory()