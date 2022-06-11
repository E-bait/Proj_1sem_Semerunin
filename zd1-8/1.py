from random import randint
n = int(input("Число: "))
b = [randint(1,20) for i in range(n)]
def Sum(b):
    if len(b)==0:
        return 0
    else:
        return Sum(b[:-1])+b[-1]
print(b)
print(Sum(b))