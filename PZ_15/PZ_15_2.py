# V 23
# В квадратной матрице все элементы, не лежащие на главной диагонали увеличить в 2 раза.

import numpy
import random

N = int(input("Введите размер матрицы: "))
arr = [[random.randint(1, 9) for i in range(N)] for j in range(N)]
print(numpy.array(arr))
for i in range(N):
    for j in range(N):
        if [i] != [j]:
            arr[i][j] *= 2
print(numpy.array(arr))
