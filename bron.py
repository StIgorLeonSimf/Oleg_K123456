from tkinter import *

root = Tk()
root.title('Бронирование')
root.geometry('450x400')

frame1 = Frame(root)
frame1.pack(pady=10, padx=50)

frame2 = Frame(root)
frame2.pack()

screen = Label(frame1, text='Экран')
screen.pack(padx=150)
canvas = Canvas(frame1, width=400, height=50)
canvas.pack()
canvas.create_line(50, 10, 350, 10, width=8, fill='light blue')
canvas.create_line(60, 40, 140, 40, width=5, fill='light green')
canvas.create_text(100, 30, text='600')
canvas.create_line(160, 40, 240, 40, width=5, fill='blue')
canvas.create_text(200, 30, text='500')
canvas.create_line(260, 40, 340, 40, width=5, fill='yellow')
canvas.create_text(300, 30, text='400')


def handler(nm, i, j):
    btns[nm - 1].config(bg='lightgray')
    ticket = Toplevel(root)
    ticket.title('Билет в кино')
    ticket.geometry('300x100')
    prompt = Label(ticket, text=f'Ряд № {i}, место {j} ')
    prompt.pack()


def free(event, nm, i):
    if i >= 0 and i < 4:
        color = 'light green'
    elif i >= 4 and i < 7:
        color = 'blue'
    else:
        color = 'yellow'
    btns[nm - 1].config(bg=color)

color = 'light green'
row = 10
column = 15
btns = []
for i in range(row):
    lab = Label(frame2, text=f'Ряд № {i + 1}')
    lab.grid(row=i, column=0)
    for j in range(column):
        num = i * column + j + 1

        if i >= 0 and i < 4:
            color = 'light green'
        elif i >= 4 and i < 7:
            color = 'blue'
        else:
            color = 'yellow'

        btn = Button(frame2)
        btn.config(text=j + 1, width=2, justify='center',
                   bg=color, command=lambda x=num, r=i + 1, seat=j + 1: handler(x, r, seat))
        btn.grid(row=i, column=j + 1)
        btn.bind('<Button-3>', lambda event, nm=num, r=i: free(event, nm, r))

        btns.append(btn)

# btn2 = Button(frame2)
# btn2.config(text=2, width=2, justify='center', bg=color)
# btn2.grid(row=0, column=1)


root.mainloop()
