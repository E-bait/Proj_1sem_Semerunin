# Вариант 23
# Описать функцию TrianglePS(a, P, S), вычисляющую по стороне a равностороннего треугольника его периметр P = 3*a
# и площадь S = a2 √3/4 (a — входной, P и S — выходные параметры; все параметры являются вещественными).
# С помощью этой функции найти периметры и площади трех равносторонних треугольников с данными сторонами.
import math


def triangleps(a):
    p = 3 * a
    s = a * a *(math.sqrt(3)/4)
    return p, s



try:
    for i in range(3):                        # Задаем значения для 3 треугольников
        znach = float(input('Введите число: '))
        per, ploch = triangleps(znach)
        print('a = ', znach)
        print('P = {0}'.format(round(per, 2)))
        print('S = {0}'.format(round(ploch, 2)))
        print()
except ValueError:
    print('Что-то пошло не так, введите число')
