"""
Апи клиент для проверки API сервиса https://jsonplaceholder.typicode.com/"
"""
import requests


class JplApiClient:
    """класс для проверки API сервиса https://jsonplaceholder.typicode.com/"""

    def __init__(self, base_url="https://jsonplaceholder.typicode.com"):
        self.session = requests.Session()
        self.session.headers = {"Content-Type": "application/json"}
        self.base_url = base_url

    def get_all_posts(self):
        """функция для эндпоинта получения всех ресурсов"""
        response = self.session.get(f"{self.base_url}/posts")
        return response

    def get_post_id(self):
        """функция получения списка id всех ресурсов"""
        response = self.session.get(f"{self.base_url}/posts")
        response_json = response.json()
        list_id = []
        for item in response_json:
            item_id = item["id"]
            list_id.append(item_id)
        return list_id

    def get_post_by_id(self, post_id):
        """функция для эндпоинта получения ресурса по id"""
        response = self.session.get(f"{self.base_url}/posts/{post_id}")
        return response

    def create_post(self, data_post):
        """функция для эндпоинта создания ресурса"""
        response = self.session.post(f"{self.base_url}/posts", json=data_post)
        return response

    def delete_post_by_id(self, post_id):
        """функция для эндпоинта удаления ресурса по id"""
        response = self.session.delete(f"{self.base_url}/posts/{post_id}")
        return response
