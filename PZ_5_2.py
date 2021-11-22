import math


def triangle(a):
    p = 3 * a
    s = math.sqrt(3) / 4 * a * a
    return p, s


for i in range(3):
    znach = float(input('Введите число: '))
    per, ploch = triangle(znach)
    print('a = ', znach)
    triangle(znach)
    print('P = {0}'.format(round(per, 2)))
    print('S = {0}'.format(round(ploch, 2)))
    print()
