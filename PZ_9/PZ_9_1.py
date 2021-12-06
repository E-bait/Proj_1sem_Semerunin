# 23 Вариант
# Дан список игрушек. Некоторые игрушки из этого списка имеются в N детских садах.
# Определить, каких игрушек их этого списка нет ни в одном из детских садов и какие есть в каждом из них.

a = {'кукла', 'машинка', 'робот', 'пазл'}
dom_1 = {'кукла', 'робот'}
dom_2 = {'машинка', 'робот'}
dom_3 = {'кукла', 'робот'}
q = dom_1 & dom_2 & dom_3
print('Игрушки которые есть во всех садах: {0} '.format(*q))
for i in a:
    if i not in (dom_1 | dom_2 | dom_3):
        print('Игрушки нет ни в одном из садов:',i)
