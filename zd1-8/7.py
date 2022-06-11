from random import randint


def maxl(l):
    if len(l)>1:
        Max = maxl(l[1:])
        if l[0] < Max:
            return Max
        else:
            return l[0]
    if len(l)==1:
        return l[0]

    
k = [randint(10,2000) for i in range(10)]
print(k)
print(maxl(k))