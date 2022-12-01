import pytest
import json
from rest_framework.test import APIClient
from model_bakery import baker

from goods.models import Good, Category


@pytest.fixture()
def client():
    return APIClient()


def test_api_availability(client):
    response = client.get('/api/v1/')
    assert response.status_code == 200


'''Testing Goods API'''

@pytest.mark.django_db
def test_get_goods(client):
    goods = baker.make(Good, _quantity=10)
    # Get_list API
    response = client.get('/api/v1/goods/goods')
    assert response.status_code == 200
    assert len(response.json()['data']) == len(goods)


@pytest.mark.django_db
def test_retrieve_get_goods(client):
    goods = baker.make(Good, _quantity=10)
    # Get_retrieve API
    response = client.get(f'/api/v1/goods/goods/{goods[0].id}')
    data = response.json()['data']
    assert response.status_code == 200
    assert data.get('id') == goods[0].id
    assert data.get('name') == goods[0].name


@pytest.mark.django_db
def test_post_api(client):
    # Post API
    goods_count = Good.objects.count()
    good = {}


@pytest.mark.django_db
def test_delete_api(client):
    goods = baker.make(Good, _quantity=10)
    goods_count: int = Good.objects.count()
    response = client.delete(f'/api/v1/goods/goods/{goods[0].id}')
    assert response.status_code == 405
    assert Good.objects.count() == goods_count



