"""
Программа создания базового класса геометрической фигуры (Figure)
Версия 1.1
"""
from abc import ABC, abstractmethod


class Figure(ABC):
    """базовый класс Фигура"""
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_area(self):
        """функция расчета площади фигуры"""
        raise NotImplementedError

    @abstractmethod
    def get_perimeter(self):
        """функция расчета периметра фигуры"""
        raise NotImplementedError


    def add_area(self, other_figure):
        """функция расчета суммы площадей фигур"""
        if not isinstance(other_figure, Figure):
            raise ValueError("Нужен класс Figure или дочерний")
        return self.get_area() + other_figure.get_area()
