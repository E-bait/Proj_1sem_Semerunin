from math import pi

_default_radius = 5


def circle_perimeter(rad=_default_radius):
    return print('Длина окружности: ', 2 * pi * rad)


def circle_area(rad=_default_radius):
    return print('Площадь окружности: ', pi * rad ** 2)
