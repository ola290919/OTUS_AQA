"""
Программа реализации класса геометрических фигур Круг
Версия 1.1
"""
import math
from src.Figure import Figure

class Circle(Figure):
    """класс Круг"""

    def __init__(self, radius: int):
        super().__init__(name="Circle")
        if radius <= 0:
            raise ValueError("радиус круга должен быть положительным числом")
        self.radius = radius

    def get_perimeter(self):
        """периметр Круга"""
        return math.pi * self.radius * 2

    def get_area(self):
        """площадь Круга"""
        return math.pi * (self.radius ** 2)

