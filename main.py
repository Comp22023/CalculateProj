from tkinter import *
#Калькулятор

def btn_click(item):
    global expression
    try:
        datafield['state'] = "normal"
        expression += item
        datafield.insert(END, item)

        if item == '=':
            result = str(eval(expression[:-1]))
            datafield.insert(END, result)
            expression = ""

        datafield['state'] = "readonly"
    except ZeroDivisionError:
        datafield.delete(0, END)
        datafield.insert(0, 'Ошибка (деление на 0)')
    except SyntaxError:
        datafield.delete(0, END)
        datafield.insert(0, 'Ошибка')

def bt_clear():
    global expression
    expression = ""
    datafield['state'] = "normal"
    datafield.delete(0, END)
    datafield['state'] = "readonly"

root = Tk() #Создание объекта

root.geometry("268x288+200+100")#Размер окна
root.title("Калькулятор by 4IP")#Заголовок


root.resizable(0, 0)
frame_calcul = Frame(root)#Создание виджета
frame_calcul.grid(row=0, column=0, columnspan=4, sticky="nsew")#Оформление виджета сеткой



def get_rgb(rgb):
    return "#%02x%02x%02x" % rgb
datafield = Entry(frame_calcul, font='Arial 15 bold', width=30, state="readonly", foreground="#004D40")
datafield.pack(fill=BOTH)

buttons = (('7', '8', '9', '/', '4'),
           ('4', '5', '6', '*', '4'),
           ('1', '2', '3', '-', '4'),
           ('0', '.', '=', '+', '4')
           )

expression = ""

buttons = (('7', '8', '9', '/', '4'),
           ('4', '5', '6', '*', '4'),
           ('1', '2', '3', '-', '4'),
           ('0', '.', '=', '+', '4')
           )


button = Button(root, text='C', background=get_rgb((128, 203, 196)), font="helvetica 15", foreground="purple", command=lambda: bt_clear())
button.grid(row=1, column=3, sticky="nsew")

for row in range(4):
    for col in range(4):
        Button(root, width=2, height=3, text=buttons[row][col], background=get_rgb((128, 203, 196)), font="helvetica 15", foreground="purple",
               command=lambda row=row, col=col: btn_click(buttons[row][col])).grid(row=row + 2, column=col, sticky="nsew", padx=1, pady=1)



root.mainloop()
#Комментарий в ветке main после merge