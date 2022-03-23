from math import sqrt


def triangle_perimeter(a=7, b =2, c=8):
    return print('Периметр треугольника: ', a + b + c)


def triangle_area(a=7, b=2, c=8):
    p = (a + b + c) / 2
    return print('Площадь треугольника: ', sqrt(p * (p - a) * (p - b) * (p - c)))
