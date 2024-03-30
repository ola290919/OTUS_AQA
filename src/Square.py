"""
Программа реализации класса геометрических фигур Квадрат
Версия 1.1
"""
from src.rectangle import Rectangle


class Square(Rectangle):
    """класс Квадрат"""

    def __init__(self, side_a):
        if 0 >= side_a:
            raise ValueError('сторона квадрата должна быть положительным числом')
        super().__init__(side_a, side_a)
        self.name = "Square"
