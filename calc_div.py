import math
from tkinter import *


def add(n1, d1, n2, d2):
    n1 *= d2
    n2 *= d1
    n = n1 + n2
    d = d1 * d2
    return n, d


def calc():
    try:
        n1 = int(num1.get())
        d1 = int(den1.get())
        n2 = int(num1.get())
        d2 = int(den1.get())
        operator = oper.get().strip()

        if operator == "+":
            result = add(n1, d1, n2, d2)
        elif operator == '-':
            pass
        elif operator == '*':
            pass
        elif operator == '/':
            pass
    except ValueError:
        pass

    nod = math.gcd(result[0], result[1])
    n = result[0] / nod
    d = result[1] / nod
    if n > d:
        int_p = n // d
        n %= d


root = Tk()
X = root.winfo_screenwidth()
Y = root.winfo_screenheight()
WIDTH = 400
HEIGHT = 200
root.geometry(f'{WIDTH}x{HEIGHT}+{X // 2 - WIDTH // 2}'
              f'+{Y // 2 - HEIGHT // 2}')
root.title('Калькулятор дробей')

frame = Frame(root)
frame.pack(pady=15)
num1 = Entry(frame)
num1.config(width=3, font='Arial 20', justify='center')
num1.grid(row=0, column=0)
line1 = Label(frame, text='----------')
line1.grid(row=1, column=0)
den1 = Entry(frame)
den1.config(width=3, font='Arial 20', justify='center')
den1.grid(row=2, column=0)

oper = Entry(frame)
oper.config(width=2, font='Arial 20', justify='center')
oper.grid(row=1, column=1, padx=5)

num2 = Entry(frame)
num2.config(width=3, font='Arial 20', justify='center')
num2.grid(row=0, column=2)
line2 = Label(frame, text='----------')
line2.grid(row=1, column=2)
den2 = Entry(frame)
den2.config(width=3, font='Arial 20', justify='center')
den2.grid(row=2, column=2)

btn = Button(frame, text='=', font='Arial 15', justify='center', command=calc)
btn.grid(row=1, column=3, padx=5)

int_part = Label(frame, text='   ')
int_part.config(width=3, font='Arial 20', justify='center', bg='lightgray')
int_part.grid(row=1, column=4)

numr = Label(frame)
numr.config(width=3, font='Arial 20', justify='center', bg='lightgray')
numr.grid(row=0, column=5)
liner = Label(frame, text='----------')
liner.grid(row=1, column=5)
denr = Label(frame)
denr.config(width=3, font='Arial 20', justify='center', bg='lightgray')
denr.grid(row=2, column=5)

root.mainloop()
