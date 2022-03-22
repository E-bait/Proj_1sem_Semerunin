# v 23
# В матрице найти максимальный положительный элемент, кратный 4.

import random
N = int(input("Введите размер матрицы:"))
arr = [[random.randint(1, 9) for i in range(N)] for j in range(N)]  # матрица
m = 0

for i in range(N):
    for j in range(N):
        if (arr[i][j] % 4 == 0) and arr[i][j] > m:                 # находим максимальное число кратное 4
            m = arr[i][j]


for i in range(N):                                             # выводим матрицу
    print(arr[i])

if m != 0:
    print('Максимальный элемент кратный 4 = ', m)
else:
    print('Элемент не найден')
