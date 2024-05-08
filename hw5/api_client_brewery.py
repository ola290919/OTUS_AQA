"""
Апи клиент для проверки API сервиса https://www.openbrewerydb.org/"
"""
import requests


class BreweryApiClient:
    """класс для проверки API сервиса https://www.openbrewerydb.org/"""

    def __init__(self, base_url="https://api.openbrewerydb.org"):
        self.session = requests.Session()
        self.session.headers = {"Content-Type": "application/json"}
        self.base_url = base_url

    def get_all_breweries(self):
        """функция для эндпоинта получения всех пивоваренных заводов"""
        response = self.session.get(f"{self.base_url}/v1/breweries")
        return response

    def get_breweries_id(self):
        """функция получения списка id пивоваренных заводов"""
        response = self.session.get(f"{self.base_url}/v1/breweries")
        response_json = response.json()
        list_id = []
        for item in response_json:
            item_id = item["id"]
            list_id.append(item_id)
        return list_id

    def get_brewery_by_id(self, brewery_id):
        """функция для эндпоинта получения пивоварни по id"""
        response = self.session.get(f"{self.base_url}/v1/breweries/{brewery_id}")
        return response

    def get_filtered_list_breweries(self, query):
        """функция для эндпоинта отфильтровать пивоварни по типу пивоварни"""
        response = self.session.get(f"{self.base_url}/v1/breweries", params=query)
        return response
