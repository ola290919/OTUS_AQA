"""
Программа реализации класса геометрических фигур Треугольник
Версия 1.1
"""
from src.Figure import Figure


class Triangle(Figure):
    """класс Треугольник"""

    def __init__(self, side_a: int, side_b: int, side_c: int):
        super().__init__(name="Triangle")
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("сторона треугольника должна быть положительным числом")
        if side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
            raise ValueError("треугольник создать нельзя - не выполнено условие неравенства треугольника")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_perimeter(self):
        """периметр Треугольника"""
        return self.side_a + self.side_b + self.side_c

    def get_area(self):
        """площадь Треугольника"""
        p = (self.side_a + self.side_b + self.side_c) / 2
        return (p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c)) ** 0.5

