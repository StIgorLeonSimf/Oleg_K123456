import time
from tkinter import *
from tkinter import messagebox

import pygame as pg

pg.init()
pg.mixer.music.load('music.mp3')


def tick():
    global alarm_time
    time_n = time.strftime('%X')
    if (alarm_time == time_n or
            alarm_time == time.strftime('%H:%M') or
            alarm_time == time.strftime('%H')):
        pg.mixer.music.play()
        alarm_time = ''
    time_now.config(text=time_n)
    time_now.after(1000, tick)


def start():
    global alarm_time
    alarm_time = alarm.get().strip()
    messagebox.showinfo('Время будильника',
                        f'Будильник установлен на {alarm_time}')


def stop():
    global alarm_time
    alarm_time = ''
    alarm.delete(0, END)
    pg.mixer.music.stop()
    messagebox.showinfo('Предупреждение',
                        f'Будильник отключён')


root = Tk()
root.geometry('400x250+400+200')
root.title('Будильник')
root.config(bg='black')

time_now = Label(text='00:00:00', font='Arial 50', bg='black', fg='lime')
time_now.pack(pady=10)

alarm = Entry(root)
alarm.config(width=10, justify='center', font='Arial 20')
alarm.pack()

btn_on = Button(root)
btn_on.config(width=10, text='Включить', font='Arial 10', command=start)
btn_on.pack(pady=10)

btn_off = Button(root)
btn_off.config(width=10, text='Выключить', font='Arial 10', command=stop)
btn_off.pack()

alarm_time = ''
tick()

root.mainloop()
