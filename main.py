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
    except:
        pass

def bt_clear():
    global expression
    expression = ""
    datafield['state'] = "normal"
    datafield.delete(0, END)
    datafield['state'] = "readonly"

root = Tk()
root.geometry("400x400")#Размер окна
root.title("Калькулятор by 4IP")#Заголовок
root.resizable(0, 0)
frame_calcul = Frame(root)#Создание виджета
frame_calcul.grid(row=0, column=0, columnspan=4, sticky="nsew")#Оформление виджета сеткой

datafield = Entry(frame_calcul, font='Arial 15 bold', width=24, state="readonly")
datafield.pack(fill=BOTH)

expression = ""


button = Button(root, text='C', command=lambda: bt_clear())
button.grid(row=1, column=3, sticky="nsew")

for row in range(4):
    for col in range(4):
        Button(root, width=2, height=3, text=buttons[row][col],
               command=lambda row=row, col=col: btn_click(buttons[row][col])).grid(row=row + 2, column=col, sticky="nsew", padx=1, pady=1)


root.mainloop()