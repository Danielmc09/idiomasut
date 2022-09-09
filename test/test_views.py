import pytest
from faker import Faker
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "idiomasut.settings")
import django
django.setup()

from app.centroidiomas.models import Salon

faker = Faker()

@pytest.fixture
def salon_create():
    return Salon(
        salo_nombre=faker.name(),
        salo_bloque='bloque33'
    )

@pytest.mark.django_db
def test_salon_creation(salon_create):
    salon_create.save()
    assert salon_create.salo_bloque == 'bloque33'
