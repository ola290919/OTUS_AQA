"""
Тесты для для проверки API сервиса https://dog.ceo/dog-api/"
"""

import pytest

from hw5.api_client_dogs import DogsApiClient

from hw5.models import DogBaseModel, DogImageBaseModel, DogImagesBaseModel

client = DogsApiClient()
breed_list = client.breeds_list()


def test_get_all_breeds():
    """Позитивный тест проверки статус-кода, наличия тела ответа,
    соответствия тела ответа модели"""
    response = client.get_all_breeds()
    response_json = response.json()
    DogBaseModel.model_validate(response_json)
    assert response.status_code == 200, "response status_code should be 200"
    assert response_json, "response body_type should be json"


@pytest.mark.parametrize("data", breed_list)
def test_get_breed_image(data):
    """Позитивный тест проверки статус-кода, наличия тела ответа для всех имеющихся пород,
    соответствия тела ответа модели"""
    response = client.get_breed_random_image(breed=data)
    response_json = response.json()
    response_model = DogImageBaseModel.model_validate(response_json)
    assert response.status_code == 200, "response status_code should be 200"
    assert response.json(), "response body_type should be json"
    assert 'https://' and '.jpg' in response_model.message


@pytest.mark.parametrize("data",
                         ["null", "0akita",
                          "aki ta", "aki-ta",
                          "     ", "1akita",
                          "-11akita", "dog",
                          "!$%akita"])
def test_get_breed_image_neg(data):
    """Негативный тест проверки невалидного названия породы:
    - "null"
    - 0 с валидным значением
    - пробел внутри валидного значения
    - дефис внутри валидного значения
    - пробелы
    - положительное число с валидным значением
    - отрицательное число с валидным значением,
    - отсутсвующая в списке порода,
    - спецсимволы с валидным значением"""
    response = client.get_breed_random_image(breed=data)
    assert response.status_code == 404, "response status_code should be 404"


def test_random_image():
    """Позитивный тест проверки статус-кода, наличия тела ответа в формате json,
    соответствия тела ответа модели"""
    response = client.get_random_image()
    response_json = response.json()
    response_model = DogImageBaseModel.model_validate(response_json)
    assert response.status_code == 200, "response status_code should be 200"
    assert response_json, "response body_type should be json"
    assert 'https://' and '.jpg' in response_model.message


@pytest.mark.parametrize("data", breed_list)
def test_get_breed_images(data):
    """Позитивный тест проверки статус-кода, наличия тела ответа для всех имеющихся пород,
    соответствия тела ответа модели"""
    response = client.get_breed_images(breed=data)
    response_json = response.json()
    DogImagesBaseModel.model_validate(response_json)
    assert response.status_code == 200, "response status_code should be 200"
    assert response_json, "response body_type should be json"
