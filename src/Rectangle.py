"""
Программа реализации класса геометрических фигур Прямоугольник
Версия 1.1
"""
from src.Figure import Figure


class Rectangle(Figure):
    """класс Прямоугольник"""
    def __init__(self, side_a: int, side_b: int):
        super().__init__(name="Rectangle")
        if side_a <= 0 or side_b <= 0:
            raise ValueError("сторона прямоугольника должна быть положительным числом")
        self.side_a = side_a
        self.side_b = side_b

    def get_area(self):
        """площадь Прямоугольника"""
        return self.side_a * self.side_b

    def get_perimeter(self):
        """периметр Прямоугольника"""
        return 2 * (self.side_a + self.side_b)
