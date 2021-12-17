# Вариант 23
# Средствами языка Python сформировать два текстовых файла (.txt),
# содержащих по одной последовательности из целых положительных и отрицательных чисел.
# Сформировать новый текстовый файл (.txt) следующего вида,
# предварительно выполнив требуемую обработку элементов:
# Содержимое первого файла: Четные элементы:
# Произведение четных элементов: Минимальный элемент:
# Содержимое второго файла: Нечетные элементы:
# Количество нечетных элементов: Сумма нечетных элементов:

import random
list1 = []
list2 = []
q = 1
s = 0

f2 = open('Negative.txt', 'w')                     # Открываем файл для записи в него отрицательной последовательности
negative = [random.randint(-100, -1) for i in range(10)]     # генерируем значения
f2.write(str(negative))
f2.close()

f1 = open('Positive.txt', 'w')                    # Открываем файл для записи в него положительной последовательности
positive = [random.randint(1, 100) for j in range(10)]            # генерируем значения
f1.write(str(positive))
f1.close()

f2 = open('Negative.txt', 'r')                  # Забираем элементы
r = f2.read()
f2.close()

f1 = open('Positive.txt', 'r')                  # Забираем элементы
rd = f1.read()
f1.close()

f2 = open('Negative.txt')             # работа с условием 1 файла
for i in negative:
    if i % 2 != 0:
        list2.append(i)
        s += i
lens = len(list2)
f2.close()

f1 = open('Positive.txt')             # работаем с условием 2 файла
for i in positive:
    if i % 2 == 0:
        list1.append(i)
        q *= i
k = min(positive)
f1.close()

t = open('Res.txt', 'w')                       # записываем результаты в 3 файл
t.write(f'Содержимое первого файла:{rd} \n')
t.write(f'Четные элементы:{" ".join(map(str,list1))} \n')
t.write(f'Произведение четных элементов:{q} \n')
t.write(f'Минимальный элемент:{k} \n')
t.write(f'Содержимое второго файла:{r} \n')
t.write(f'Нечетные элементы:{" ".join(map(str,list2))} \n')
t.write(f'Кол-во нечетных элементов:{lens} \n')
t.write(f'Сумма нечетных элементов:{s}')
t.close()
