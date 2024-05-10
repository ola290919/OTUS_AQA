"""
Тесты для для проверки API сервиса https://www.openbrewerydb.org/"
"""

import pytest

from hw5.api_client_brewery import BreweryApiClient

from hw5.models import BreweryBaseModel

client = BreweryApiClient()
id_list = client.get_breweries_id()


def test_get_all_breweries():
    """Позитивный тест проверки статус-кода, наличия тела ответа,
    соответствия тела ответа модели"""
    response = client.get_all_breweries()
    response_json = response.json()
    brewery = [BreweryBaseModel.model_validate(obj) for obj in response_json]
    assert response.status_code == 200, "response status_code should be 200"
    assert response_json, "response body_type should be json"


@pytest.mark.parametrize("data", id_list)
def test_get_brewery_by_id(data):
    """Позитивный тест проверки статус-кода, наличия тела ответа для всех имеющихся ресурсов,
    соответствия тела ответа модели"""
    response = client.get_brewery_by_id(brewery_id=data)
    response_json = response.json()
    BreweryBaseModel.model_validate(response_json)
    assert response.status_code == 200, "response status_code should be 200"
    assert response.json(), "response body_type should be json"


@pytest.mark.parametrize("data",
                         ["null", "0", "fe6b 9893-b93e-43d5-a9f6-3e0c89a3f13c",
                          "fe6b9893--b93e-43d5-a9f6-3e0c89a3f13c",
                          "     ", "-fe6b9893-b93e-43d5-a9f6-3e0c89a3f13c", "100500",
                          "fe6b9893-b93e-43d5-a9f6-3e0c89a3f13c!$%"])
def test_get_brewery_by_id_neg(data):
    """Негативный тест проверки невалидного id:
    - "null"
    - 0
    - пробел внутри валидного значения
    - дефис внутри валидного значения
    - пробелы
    - отрицательное число,
    - несуществующий id,
    - спецсимволы с валидным значением"""
    response = client.get_brewery_by_id(brewery_id=data)
    assert response.status_code == 404, "response status_code should be 404"


@pytest.mark.parametrize("by_type",
                         ['micro', 'nano', 'regional', 'brewpub',
                          'large', 'planning', 'bar', 'contract', 'proprietor',
                          'closed'])
def test_filter_brewery(by_type):
    """Позитивный тест проверки статус-кода, наличия тела ответа,
        соответствия тела ответа модели"""
    query = {"by_type": by_type}
    response = client.get_filtered_list_breweries(query)
    brewery = [BreweryBaseModel.model_validate(obj) for obj in response.json()]
    assert response.status_code == 200, "response status_code should be 200"


@pytest.mark.parametrize("by_type",
                         ['0', 'na no', 'reg-ional', '     ',
                          '1large', '-11planning', 'big', '!@#$%^contract'])
def test_filter_brewery_neg(by_type):
    """Негативный тест проверки невалидного типа:
        - 0
        - пробел внутри валидного значения
        - дефис внутри валидного значения
        - пробелы
        - число с валидным значением
        - отрицательное число с валидным значением,
        - несуществующий тип,
        - спецсимволы с валидным значением"""
    query = {"by_type": by_type}
    response = client.get_filtered_list_breweries(query)
    assert response.status_code == 400, "response status_code should be 400"
