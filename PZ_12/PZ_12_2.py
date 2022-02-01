# Вариант 23
# PZ_5_2
# Описать функцию TrianglePS(a, P, S), вычисляющую по стороне a равностороннего треугольника его периметр P = 3*a
# и площадь S = a2 √3/4 (a — входной, P и S — выходные параметры; все параметры являются вещественными).
# С помощью этой функции найти периметры и площади трех равносторонних треугольников с данными сторонами.
from tkinter import *
import math


def triangle():
    a = float(number_entry.get())
    p = 3 * a
    s = math.sqrt(3) / 4 * a * a
    res_1_end.config(text='S={0}'.format(round(s, 2)))
    res_1_end1.config(text='P={0}'.format(round(p, 2)))
    b = float(number1_entry.get())
    per = 3 * b
    ploch = math.sqrt(3) / 4 * b * b
    res_2_end.config(text='S={0}'.format(round(ploch, 2)))
    res_2_end1.config(text='P={0}'.format(round(per, 2)))
    x = float(number2_entry.get())
    pr = 3 * x
    pl = math.sqrt(3) / 4 * x * x
    res_3_end.config(text='S={0}'.format(round(pl, 2)))
    res_3_end1.config(text='P={0}'.format(round(pr, 2)))


root = Tk()
root.title("Triangle")
root.columnconfigure(0, weight=1)
root.columnconfigure(3, weight=2)
root.rowconfigure(0, weight=0)
root.columnconfigure(1, weight=0)
root.geometry('350x250')
root.resizable(0, 0)
root['bg'] = '#FFFFE0'

lbl = Label(root, text='P и S равностороннего треугольника', font='Arial 11', bg='#7B68EE', fg='#F0E68C')
lbl.grid(row=0, column=0, sticky=W+E)

number_label = Label(root, text='Введите число a1:', font='Times 11', bg='#FFFFE0')
number_label.grid(row=1, sticky=W, padx=5, pady=5)

number_entry = Entry(root, width=30, bd=2)
number_entry.grid(row=1, column=0, sticky=W, columnspan=2, padx=125, pady=5)

number1_label = Label(root, text='Введите число a2:', font='Times 11', bg='#FFFFE0')
number1_label.grid(row=2, sticky=W, padx=5, pady=5)

number2_label = Label(root, text='Введите число a3:', font='Times 11', bg='#FFFFE0')
number2_label.grid(row=3, sticky=W, padx=5, pady=5)

number1_entry = Entry(root, width=30, bd=2)
number1_entry.grid(row=2, column=0, sticky=W, columnspan=2, padx=125, pady=5)

number2_entry = Entry(root, width=30, bd=2)
number2_entry.grid(row=3, column=0, sticky=W, columnspan=2, padx=125, pady=5)

res_but = Button(root, text='результат', font='Times 11', bg='#1E90FF', command=triangle)
res_but.grid(row=4, sticky=W+E, padx=8, pady=10)

res_1 = Label(root, text='Result 1:', font='Times 11', bg='#FFFFE0')
res_1.grid(row=5, sticky=W, padx=5)

res_1_end = Label(root, text='', bg='#FFFFE0')
res_1_end.grid(row=6, sticky=W, padx=8, pady=0)

res_1_end1 = Label(root, text='', bg='#FFFFE0')
res_1_end1.grid(row=7, sticky=W, padx=8, pady=0)

res_2 = Label(root, text='Result 2:', font='Times 11', bg='#FFFFE0')
res_2.grid(row=5, sticky=W, padx=135)

res_2_end = Label(root, text='', bg='#FFFFE0')
res_2_end.grid(row=6, sticky=W, padx=136, pady=0)

res_2_end1 = Label(root, text='', bg='#FFFFE0')
res_2_end1.grid(row=7, sticky=W, padx=136, pady=0)

res_3 = Label(root, text='Result 3:', font='Times 11', bg='#FFFFE0')
res_3.grid(row=5, sticky=E, padx=40)

res_3_end = Label(root, text='', bg='#FFFFE0')
res_3_end.grid(row=6, sticky=E, padx=42, pady=0)

res_3_end1 = Label(root, text='', bg='#FFFFE0')
res_3_end1.grid(row=7, sticky=E, padx=42, pady=0)

root.mainloop()
