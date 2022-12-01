import pytest
import json

from rest_framework.test import APIClient
from django.db.models import Model

from model_bakery import baker
from goods.models import Good, Category


TEST_METHODS: list[str] = []
TEST_MODEL: Model = None
TEST_API_URI: str = None





@pytest.fixture()
def client():
    return APIClient()


@pytest.mark.django_db
def test_get_list(client):
    units = baker.make(TEST_MODEL, _quantity=10)
    # Get_list API
    response = client.get(TEST_API_URI)
    assert response.status_code == 200
    assert len(response.json()['data']) == len(units)


@pytest.mark.django_db
def test_retrieve_get(client):
    units = baker.make(TEST_MODEL, _quantity=10)
    # Get_retrieve API
    response = client.get(f'{TEST_API_URI}{units[0].id}')
    data = response.json()['data']
    assert response.status_code == 200
    assert data.get('id') == units[0].id
    assert data.get('name') == units[0].name


@pytest.mark.django_db
def test_post_api(client):
    # Post API
    units_count = TEST_MODEL.objects.count()
    unit = {}


@pytest.mark.django_db
def test_delete_api(client):
    units = baker.make(TEST_MODEL, _quantity=10)
    units_count: int = TEST_MODEL.objects.count()
    response = client.delete(f'{TEST_API_URI}{units[0].id}')
    assert response.status_code == 204
    assert TEST_MODEL.objects.count() == units_count - 1

@pytest.mark.django_db
def testing():#TEST_METHODS: list[str] = [],
            # TEST_MODEL: Model = Good,
            # TEST_API_URI: str = None):
    test_get_list(client)
pass
