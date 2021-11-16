# import json
# from unittest import mock

import pytest

from .core.factories import PsychologistFactory

# from rest_framework import status
# from rest_framework.test import APIClient


@pytest.fixture
def Psychologist_object():
    return PsychologistFactory()
