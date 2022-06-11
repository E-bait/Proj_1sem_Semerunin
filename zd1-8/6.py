def Power(x,y):
    if y>0:
        return x * Power(x,y-1)
    else:
        return 1

print('Result: ',Power(2,4))