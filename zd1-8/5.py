num = int(input("Введите число: "))
revers_num = 0
def recur(num):
    global revers_num
    if (num > 0):
        Reminder = num % 10
        revers_num = (revers_num * 10) + Reminder
        recur(num // 10)
    return revers_num


revers_num = recur(num)
print(f"Res: {revers_num}")
