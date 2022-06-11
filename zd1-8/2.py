from random import randint
b = [randint(-10,20) for i in range(10)]
def negative(b):
    if len(b) == 0:
        return 0
    else:
        count = negative(b[1:])
        if b[0] < 0:
            count+=1
        return count

print(b)
print(negative(b))