# 23 вариант
# Дан список A размера N. Сформировать новый список B того же размера, элементы которого определяются следующим образом:
# BK = 2*AK, если AK < 5,
# AK/2 в противном случае.

import random                              # импортирование модуля рандом
n = int(input('Введите размер списка: '))
a = [random.randrange(0, 10) for i in range(n)]    # генерирование списка
print('a = {0}'.format(a))
b = []
for element in a:
    if element < 5:
        b.append(2*int(element))
    else:
        b.append(element/2)
print('b = {0}'.format(b))
