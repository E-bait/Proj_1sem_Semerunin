# Вариант 23
# Из предложенного текстового файла (text18-23.txt) вывести на экран его содержимое,
# количество знаков пунктуации в первых четырёх строках.
# Сформировать новый файл, в который поместить текст в стихотворной форме предварительно заменив символы
# верхнего регистра на нижний.
f1 = open('text18-23.txt', 'r', encoding='utf-8')
print('Содержимое файла: ')                       # Выводим содержимое файла в pycharm
a = f1.read()
print(a)
f1.close()

f1 = open('text18-23.txt', 'r', encoding='utf-8')          # Находим кол-во знаков препинания в первых 4 строках
q = str()
i = 1
x = [',', ':', '.']
while i <= 4:
    t = f1.readline()
    q += t
    i += 1
j = 0
for k in range(0, len(q)):
    if q[k] in x:
        j += 1
print('кол-во знаков препинания в первых 4 строках: ', j)
f1.close()

f2 = open('text18-23-2.txt', 'w', encoding='utf-8')         # Создаем новый файл и переводим символы в нижний регистр
f2.write(a.lower())
f2.close()
