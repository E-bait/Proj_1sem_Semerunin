# Вариант 23
# Дано целое число N (>0). Найти наибольшее целое число K, квадрат которого не превосходит N: K**2 < N.
# Функцию извлечения квадратного корня не использовать.
n = input("Введите целое положительное число:")
k = 1
try:                              # Обработка исключений
    n = int(n)
    if n > 0:                       # Проверка условия
        while k * k < n:           # Нахождения K, N:K**2 < N
            k += 1
        k -= 1
        print("K = {0}, K^2 = {1}, (K+1)^2 = {2}".format(k, k ** 2, (k + 1) ** 2))
    else:
        print('Что-то пошло не так')
except ValueError:
    print('Что-то пошло не так')
