def dec_bin(N):
    if N >= 2:
        dec_bin(N // 2)
    print(N % 2, end='')

a = int(input("Введите десятичное число: "))
dec_bin(a)