"""
Классы для проверки тела запроса, ответа
"""

from typing import Literal

from typing import Optional

from pydantic import BaseModel


class DogImageBaseModel(BaseModel):
    """Класс для тела ответа эндпоинта получения случайного изображения
    сервиса https://dog.ceo/dog-api/"""
    message: str
    status: Literal['success']


class DogBaseModel(DogImageBaseModel):
    """Класс для тела ответа эндпоинта получения списка всех пород
    сервиса https://dog.ceo/dog-api/"""
    message: dict


class DogImagesBaseModel(DogImageBaseModel):
    """Класс для тела ответа эндпоинта получения изображения породы
    сервиса https://dog.ceo/dog-api/"""
    message: list


class JplBaseModel(BaseModel):
    """Класс для тела ответа эндпоинта получения ресурса
    сервиса https://jsonplaceholder.typicode.com/"""
    userId: int
    id: int
    title: str
    body: str


class JplListBaseModel(JplBaseModel):
    """Класс для тела ответа эндпоинта получения всех ресурсов
    сервиса https://jsonplaceholder.typicode.com/"""
    userId: Optional[int] = ""
    body: Optional[str] = ""


class JplDataBaseModel(JplBaseModel):
    """Класс для тела запроса эндпоинта создания  ресурса
    сервиса https://jsonplaceholder.typicode.com/"""
    id: Optional[int] = None


class BreweryBaseModel(BaseModel):
    """Класс для тела ответа эндпоинтов
    сервиса https://www.openbrewerydb.org/"""
    id: str
    name: str
    brewery_type: Literal[
        'micro', 'nano', 'regional', 'brewpub', 'large', 'planning',
        'bar', 'contract', 'proprietor', 'closed']
    address_1: Optional[str] = ""
    address_2: Optional[str] = ""
    address_3: Optional[str] = ""
    city: str
    state_province: str
    postal_code: str
    country: str
    longitude: Optional[float] = ""
    latitude: Optional[float] = ""
    phone: Optional[str] = ""
    website_url: Optional[str] = ""
    state: str
    street: Optional[str] = ""
