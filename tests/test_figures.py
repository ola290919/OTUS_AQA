"""
Тестирование класса геометрических фигур
Версия 1.1
"""
import pytest
from src.Rectangle import Rectangle
from src.Square import Square
from src.Circle import Circle
from src.Triangle import Triangle


@pytest.mark.parametrize("data_param", ["integer", "float"])
def test_rectangle_positiv(figures_data, data_param):
    """
    Позитивные тесты класса Прямоугольник:
    - расчет площади Прямоугольника
    - расчет периметра Прямоугольника
    - сумма площадей Прямоугольник + Квадрат
    - сумма площадей Прямоугольник + Треугольник
    - сумма площадей Прямоугольник + Круг
    """
    side_a, side_b, side_c, radius, area_r, perimeter_r, area_s, perimeter_s, area_t, perimeter_t, area_c, perimeter_c, add_r_s, add_r_t, add_r_c, add_s_t, add_s_c, add_t_c = figures_data(data=data_param)
    r = Rectangle(side_a, side_b)
    s = Square(side_a)
    t = Triangle(side_a, side_b, side_c)
    c = Circle(radius)
    assert r.get_area() == area_r, f"Area should be {area_r}"
    assert r.get_perimeter() == perimeter_r, f"perimeter should be {perimeter_r}"
    assert r.add_area(other_figure=s) == add_r_s, f"summ areas should be {add_r_s}"
    assert r.add_area(other_figure=t) == add_r_t, f"summ areas should be {add_r_t}"
    assert r.add_area(other_figure=c) == add_r_c, f"summ areas should be {add_r_c}"


@pytest.mark.parametrize("data_param", ["integer", "float"])
def test_square_positiv(figures_data, data_param):
    """
    Позитивные тесты класса Квадрат:
    - расчет площади Квадрата
    - расчет периметра Квадрата
    - сумма площадей Квадрат + Прямоугольник
    - сумма площадей Квадрат + Треугольник
    - сумма площадей Квадрат + Круг
    """
    side_a, side_b, side_c, radius, area_r, perimeter_r, area_s, perimeter_s, area_t, perimeter_t, area_c, perimeter_c, add_r_s, add_r_t, add_r_c, add_s_t, add_s_c, add_t_c = figures_data(data=data_param)
    r = Rectangle(side_a, side_b)
    s = Square(side_a)
    t = Triangle(side_a, side_b, side_c)
    c = Circle(radius)
    assert s.get_area() == area_s, f"Area should be {area_s}"
    assert s.get_perimeter() == perimeter_s, f"perimeter should be {perimeter_s}"
    assert s.add_area(other_figure=r) == add_r_s, f"summ areas should be {add_r_s}"
    assert s.add_area(other_figure=t) == add_s_t, f"summ areas should be {add_s_t}"
    assert s.add_area(other_figure=c) == add_s_c, f"summ areas should be {add_s_c}"


@pytest.mark.parametrize("data_param", ["integer", "float"])
def test_triangle_positiv(figures_data, data_param):
    """
    Позитивные тесты класса Треугольник:
    - расчет площади Треугольника
    - расчет периметра Треугольника
    - сумма площадей Треугольник + Прямоугольник
    - сумма площадей Треугольник + Квадрат
    - сумма площадей Треугольник + Круг
    """
    side_a, side_b, side_c, radius, area_r, perimeter_r, area_s, perimeter_s, area_t, perimeter_t, area_c, perimeter_c, add_r_s, add_r_t, add_r_c, add_s_t, add_s_c, add_t_c = figures_data(data=data_param)
    r = Rectangle(side_a, side_b)
    s = Square(side_a)
    t = Triangle(side_a, side_b, side_c)
    c = Circle(radius)
    assert t.get_area() == area_t, f"Area should be {area_t}"
    assert t.get_perimeter() == perimeter_t, f"perimeter should be {perimeter_t}"
    assert t.add_area(other_figure=r) == add_r_t, f"summ areas should be {add_r_t}"
    assert t.add_area(other_figure=s) == add_s_t, f"summ areas should be {add_s_t}"
    assert t.add_area(other_figure=c) == add_t_c, f"summ areas should be {add_t_c}"


@pytest.mark.parametrize("data_param", ["integer", "float"])
def test_circle_positiv(figures_data, data_param):
    """
    Позитивные тесты класса Круг:
    - расчет площади Круга
    - расчет периметра Круга
    - сумма площадей Круг + Прямоугольник
    - сумма площадей Круг + Квадрат
    - сумма площадей Круг + Треугольник
    """
    side_a, side_b, side_c, radius, area_r, perimeter_r, area_s, perimeter_s, area_t, perimeter_t, area_c, perimeter_c, add_r_s, add_r_t, add_r_c, add_s_t, add_s_c, add_t_c = figures_data(data=data_param)
    r = Rectangle(side_a, side_b)
    s = Square(side_a)
    t = Triangle(side_a, side_b, side_c)
    c = Circle(radius)
    assert c.get_area() == area_c, f"Area should be {area_c}"
    assert c.get_perimeter() == perimeter_c, f"perimeter should be {perimeter_c}"
    assert c.add_area(other_figure=r) == add_r_c, f"summ areas should be {add_r_c}"
    assert c.add_area(other_figure=s) == add_s_c, f"summ areas should be {add_s_c}"
    assert c.add_area(other_figure=t) == add_t_c, f"summ areas should be {add_t_c}"


def test_rectangle_negativ_a():
    """Негативный тест класса Прямоугольник - проверка сторона < 0"""
    with pytest.raises(ValueError):
        Rectangle(-3, 5)


def test_rectangle_negativ_a0():
    """Негативный тест класса Прямоугольник - проверка сторона = 0"""
    with pytest.raises(ValueError):
        Rectangle(0, 5)


def test_square_negativ():
    """Негативный тест класса Квадрат - проверка сторона < 0"""
    with pytest.raises(ValueError):
        Square(-5)


def test_square_negativ_0():
    """Негативный тест класса Квадрат - проверка сторона = 0"""
    with pytest.raises(ValueError):
        Square(0)


def test_triangle_negativ():
    """Негативный тест класса Треугольник - проверка сторона < 0"""
    with pytest.raises(ValueError):
        Triangle(3, 5, -8)


def test_triangle_negativ_a0():
    """Негативный тест класса Треугольник - проверка сторона = 0"""
    with pytest.raises(ValueError):
        Triangle(0, 5, 8)


def test_triangle_negativ_inequality():
    """Негативный тест класса Треугольник - проверка неравенства треугольника"""
    with pytest.raises(ValueError):
        Triangle(3, 5, 18)


def test_circle_negativ():
    """Негативный тест класса Круг - проверка радиус < 0"""
    with pytest.raises(ValueError):
        Circle(-5)


def test_circle_negativ_0():
    """Негативный тест класса Круг - проверка радиус = 0"""
    with pytest.raises(ValueError):
        Circle(0)

