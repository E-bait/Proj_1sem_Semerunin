# Вариант 23
# http://ip-whois.net/forma-obratnoj-svyazi/img/form1.jpg
from tkinter import *

window = Tk()
window.geometry('376x476')
window.resizable(0, 0)
window['bg'] = '#FFFFE0'
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=0)
lbl = Label(window, text='Онлайн заказ', bg='#008B8B', fg='#FFFF00', font='Times 14')
lbl.grid(row=0, column=0, sticky=E+W)

name_label = Label(window, text="Имя:", bg='#FFFFE0')
name_label.grid(row=1, sticky=W, padx=5, pady=0)
name_entry = Entry(window, width=60, bd=2)
name_entry.grid(row=2, padx=8, pady=0, sticky=W)

mail_label = Label(window, text='Адрес e-mail:', bg='#FFFFE0')
mail_label.grid(row=3, sticky=W, padx=5, pady=0)
mail_entry = Entry(window, width=60, bd=2)
mail_entry.grid(row=4, sticky=W, padx=8, pady=0)

delivery_label = Label(window, text='Адрес доставки:', bg='#FFFFE0')
delivery_label.grid(row=5, sticky=W, padx=5, pady=0)
delivery_entry = Entry(window, width=60, bd=2)
delivery_entry.grid(row=6, sticky=W, padx=8, pady=0)

phone_label = Label(window, text='Контактный телефон:', bg='#FFFFE0')
phone_label.grid(row=7, sticky=W, padx=5, pady=0)
phone_entry = Entry(window, width=60, bd=2)
phone_entry.grid(row=8, sticky=W, padx=8, pady=0)

id_label = Label(window, text='ID продукта:', bg='#FFFFE0')
id_label.grid(row=9, sticky=W, padx=5, pady=0)
id_entry = Entry(window, width=60, bd=2)
id_entry.grid(row=10, sticky=W, padx=8, pady=0)

inf_label = Label(window, text='Подробная информация о заказе:', bg='#FFFFE0')
inf_label.grid(row=11, sticky=W, padx=5, pady=0)
inf_text = Text(window, width=60, bd=2, height=8)
inf_text.grid(row=12, sticky=W, padx=8, pady=0)

numbers_label = Label(window, text='Число с картинки:', bg='#FFFFE0')
numbers_label.grid(row=13, sticky=W, padx=5, pady=0)
numbers_entry = Entry(window, width=60, bd=2)
numbers_entry.grid(row=14, sticky=W, padx=8, pady=0)

canvas = Canvas(window, height=40, width=120)
img = PhotoImage(file='123.png')
image = canvas.create_image(0, 0, anchor='nw', image=img)
canvas.grid(row=15, sticky=W, padx=8, pady=5)

send_button = Button(window, text='Отправить', width=10, height=1, bg='#1E90FF')
send_button.grid(row=15, sticky=W, padx=135, pady=2)

window.mainloop()
