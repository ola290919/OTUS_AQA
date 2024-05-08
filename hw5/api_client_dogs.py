"""
Апи клиент для проверки API сервиса https://dog.ceo/dog-api/"
"""
import requests


class DogsApiClient:
    """класс для проверки API сервиса https://dog.ceo/dog-api/"""

    def __init__(self, base_url="https://dog.ceo/api"):
        self.session = requests.Session()
        self.session.headers = {"Content-Type": "application/json"}
        self.base_url = base_url

    def get_all_breeds(self):
        """функция для эндпоинта получения всех пород"""
        response = self.session.get(f"{self.base_url}/breeds/list/all")
        return response

    def get_random_image(self):
        """функция для эндпоинта получения случайного изображения"""
        response = self.session.get(f"{self.base_url}/breeds/image/random")
        return response

    def breeds_list(self):
        """функция получения списка всех пород"""
        response = self.session.get(f"{self.base_url}/breeds/list/all")
        response_json = response.json()
        breeds_list = list(response_json["message"])
        return breeds_list

    def get_breed_random_image(self, breed):
        """функция для эндпоинта получения случайного изображения породы"""
        response = self.session.get(f"{self.base_url}/breed/{breed}/images/random")
        return response

    def get_breed_images(self, breed):
        """функция для эндпоинта получения всех изображений породы"""
        response = self.session.get(f"{self.base_url}/breed/{breed}/images")
        return response
