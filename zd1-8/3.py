def sum(lst):
    total = 0
    for element in lst:
        if (type(element) == type([])):
            total = total + sum(element)
        else:
            total = total + element
    return total
print("Сумма элементов равна:", sum([13,[1, 9,2], [3,4, 4],123]))