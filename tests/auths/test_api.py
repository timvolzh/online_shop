import pytest
import json
from rest_framework.test import APIClient
from model_bakery import baker

from auths.models import CustomUser


@pytest.fixture()
def client():
    return APIClient()


def test_api_availability(client):
    response = client.get('/api/v1/')
    assert response.status_code == 200


'''Testing Goods API'''


@pytest.mark.django_db
def test_get_list(client):
    units = baker.make(CustomUser, _quantity=10)
    response = client.get('/api/v1/auths/users')
    assert response.status_code == 200
    assert len(response.json()['data']) == len(units)


@pytest.mark.django_db
def test_retrieve_get(client):
    units = baker.make(CustomUser, _quantity=10)
    response = client.get(f'/api/v1/auths/users/{units[0].id}')
    data: dict = response.json()['data']
    assert response.status_code == 200
    assert data.get('id') == units[0].id
    assert data.get('email') == units[0].email


@pytest.mark.django_db
def test_post_api(client):
    units = baker.make(CustomUser, _quantity=10)
    units_count: int = CustomUser.objects.count()
    unit_params: dict = {"email": "ede@ya.ru",
                         "password": "Andrew_BeardStalker1995_69",
                         "first_name": "Andrew",
                         "last_name": "Borodach",
                         "is_active": "True",
                         "is_stuff": "False"
                         }
    response = client.post('/api/v1/auths/users', data=unit_params, format='json')
    assert response.status_code == 201
    assert CustomUser.objects.count() == units_count + 1


@pytest.mark.django_db
def test_delete_api(client):
    units = baker.make(CustomUser, _quantity=10)
    units_count: int = CustomUser.objects.count()
    response = client.delete(f'/api/v1/auths/users/{units[0].id}')
    assert response.status_code == 405
    assert CustomUser.objects.count() == units_count
