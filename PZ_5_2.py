# Вариант 23
# Описать функцию TrianglePS(a, P, S), вычисляющую по стороне a равностороннего треугольника его периметр P = 3*a
# и площадь S = a2 √3/4 (a — входной, P и S — выходные параметры; все параметры являются вещественными).
# С помощью этой функции найти периметры и площади трех равносторонних треугольников с данными сторонами.
import math


def triangle(a):
    p = 3 * a
    s = math.sqrt(3) / 4 * a * a
    return p, s               # Забираем p,s


for i in range(3):                        # Задаем значения для 3 треугольников
    znach = float(input('Введите число: '))
    per, ploch = triangle(znach)
    print('a = ', znach)
    triangle(znach)
    print('P = {0}'.format(round(per, 2)))
    print('S = {0}'.format(round(ploch, 2)))
    print()
