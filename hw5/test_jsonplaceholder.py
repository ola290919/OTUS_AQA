"""
Тесты для для проверки API сервиса https://dog.ceo/dog-api/"
"""

import pytest

from hw5.api_client_jsonplaceholder import JplApiClient

from hw5.models import JplBaseModel, JplListBaseModel, JplDataBaseModel

client = JplApiClient()
id_list = client.get_post_id()


def test_get_all_posts():
    """Позитивный тест проверки статус-кода, наличия тела ответа,
    соответствия тела ответа модели"""
    response = client.get_all_posts()
    response_json = response.json()
    post = [JplListBaseModel.model_validate(obj) for obj in response_json]
    assert response.status_code == 200, "response status_code should be 200"
    assert response_json, "response body_type should be json"


@pytest.mark.parametrize("data", id_list)
def test_get_post_by_id(data):
    """Позитивный тест проверки статус-кода, наличия тела ответа для всех имеющихся ресурсов,
    соответствия тела ответа модели"""
    response = client.get_post_by_id(post_id=data)
    response_json = response.json()
    JplBaseModel.model_validate(response_json)
    assert response.status_code == 200, "response status_code should be 200"
    assert response.json(), "response body_type should be json"


@pytest.mark.parametrize("data",
                         ["null", "0", "1 1", "1-1",
                          "     ", "-11", "100500", "!$%12"])
def test_get_post_by_id_neg(data):
    """Негативный тест проверки невалидного id:
    - "null"
    - 0
    - пробел внутри валидного значения
    - дефис внутри валидного значения
    - пробелы
    - отрицательное число,
    - несуществующий id,
    - спецсимволы с валидным значением"""
    response = client.get_post_by_id(post_id=data)
    assert response.status_code == 404, "response status_code should be 404"


def test_create_post():
    """Позитивный тест проверки статус-кода, наличия тела ответа,
        соответствия тела ответа модели"""
    data = JplDataBaseModel(title='foo', body='bar', userId=11)
    response = client.create_post(data_post=data.dict())
    JplBaseModel.model_validate(response.json())
    assert response.status_code == 201, "response status_code should be 201"


@pytest.mark.parametrize("data", id_list)
def test_delete_post_by_id(data):
    """Позитивный тест проверки статус-кода для удаления всех имеющихся ресурсов"""
    response = client.delete_post_by_id(post_id=data)
    assert response.status_code == 200, "response status_code should be 200"
