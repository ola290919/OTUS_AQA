"""
Фикстура для ввода через CLI 2 параметров:
url - значение по умолчанию https://ya.ru
code - значение по умолчанию 200,
значения на выбор '200', '300', '400', '404', '409', '500', '502'"

"""

import pytest


def pytest_addoption(parser):
    """функция для передачи парсера с нужными параметрами"""
    parser.addoption("--url", action="store", default="https://ya.ru", help="This is request url")
    parser.addoption("--code", action="store",
                     choices=['200', '300', '400', '404', '409', '500', '502'],
                     default='200', help="This is expected status code")


@pytest.fixture
def url(request):
    """фикстура вызов url"""
    return request.config.getoption("--url")


@pytest.fixture
def status_code(request):
    """фикстура вызов code"""
    return request.config.getoption("--code")
