# V23
# Из  исходного  текстового  файла  (ip_address.txt)
# из  раздела  «Зарезервированные адреса»
# перенести в первый файл строки с ненулевыми первым и вторым октетами,
# а  во  второй  –  все  остальные.
# Посчитать  количество  полученных  строк  в  каждом файле.

import re

with open("ip_address.txt", "r", encoding="utf-8") as initially:   # открываем для чтения
    pat = r"((\d+\.)+[\/\d+]*)"           # шаблон
    result = map(lambda x: x[0], re.findall(pat, initially.read()))   # применяем функцию к каждому объекту
    with open("two.txt", "w", encoding="utf-8") as num1, open("other.txt", "w", encoding="utf-8") as num2:
        two_zero = 0
        other_ip = 0
        for ip in result:
            if ip.split(".")[:2] == ['0', '0']:   # для ip вида 0.0
                two_zero += 1
                print(ip, file=num1)
            else:                         # другие ip
                other_ip += 1
                print(ip, file=num2)
        print(
            f"Общее кол-во строк: {two_zero}",
            file=num1
        )
        print(
            f"Общее кол-во строк: {other_ip}",
            file=num2
        )
