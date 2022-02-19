# V23
# В последовательности на n целых элементов в последней ее половине найти
# сумму элементов.
import math                     # Импортируем модули
import numpy as np
b = []


def func_chunks_num(lst, c_num):
    n = math.ceil(len(lst) / c_num)           # Делим кол-во элементов на кол-во частей

    for x in range(0, len(lst), n):
        lst1 = lst[x: n + x]
        yield lst1                        # генератор


# делим список на 2 равные части
print(list(func_chunks_num([n for n in range(1, 21)], c_num=2)))
# присваиваем значение в b
b.append(list(func_chunks_num([n for n in range(1, 21)], c_num=2)))
# выводим последнюю половину
print('Последняя половина: {0}'.format(list(b[0][1])))
# сумма элементов
total = np.sum(b[0][1])
print('сумма элементов во второй половине = {0}'.format(total))
