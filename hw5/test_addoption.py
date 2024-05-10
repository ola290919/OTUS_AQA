"""
Тестовая функция, которая принимает 2 параметра:
url - значение по умолчанию https://ya.ru
status_code - значение по умолчанию 200"
"""

import requests


def test_url_code(url, status_code):
    """Тестовая функция"""
    response = requests.get(f"{url}")
    assert f'{response.status_code}' == status_code
