# V 23
# В квадратной матрице все элементы, не лежащие на главной диагонали увеличить в 2 раза.
import numpy
import random

b = []
N = int(input("Введите размер матрицы: "))
arr = [[random.randint(1, 9) for i in range(N)] for j in range(N)]  # матрица
print(numpy.array(arr))
for i in range(N):
    for j in range(N):
        if arr[i] != arr[j]:                               # i and j индексы
            b.append(arr[i][j] * 2)                          # Умножаем элементы не находящиеся на главной диагонали
print(f'Результат:', b)
