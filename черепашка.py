from turtle import *

colormode(255)
shape('turtle')
speed(1)
# color('red')  # rgb(255, 155, 255)
# color(128, 128, 128)
color('#FF00FF', 'yellow')
pensize(5)
# fillcolor('yellow')

# begin_fill()
# forward(200)
# left(120)
# fd(100)
# lt(60)
# fd(100)
# lt(60)
# fd(100)
# end_fill()
# for i in range(9):
#     begin_fill()
#     circle(40)
#     end_fill()
#     rt(45)
x = 200
r = 255
g = 255
b = 0
for j in range(200, 149, -25):
    fillcolor(r, g, b)
    penup()
    x -= 200
    goto(x, 0)
    pendown()
    begin_fill()
    for i in range(200, 149, -25):
        fd(j)
        lt(120)
    end_fill()
    r -= 50
    g -= 25
    b += 75
# for i in range(3):
#     fd(200)
#     lt(120)
# fd(200)
# lt(120)
#
# fd(200)
# lt(120)


mainloop()
"""
0  00000000    256 0-255
1  00000001
2  00000010
3  00000011
. 
.
. 
9  00001001    9
10 00001010    A 
11             B
.
.
15             F 





"""