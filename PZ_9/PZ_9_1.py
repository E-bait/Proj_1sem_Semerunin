a = {'кукла','машинка','робот','пазл',''}
dom_1 = {'кукла','робот'}
dom_2 = {'машинка','робот'}
dom_3 = {'кукла','робот'}
q = set(dom_1&dom_2&dom_3)
print('Игрушки которые есть во всех садах: {0} '.format(*q))
for i in a:
    if i not in (dom_1|dom_2|dom_3):
        print('Игрушки нет ни в одном из садов:',i)