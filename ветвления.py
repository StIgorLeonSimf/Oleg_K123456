"""
>, <, >=, <=, ==, !=
"""
x = 8
y = 8
c = x < y and x <= y and x == y
c1 = x > y or x >= y or x == y
print(c, c1)

if x < y:
    print('X < Y')
elif x > y:
    print('X > Y')
elif x == y:
    print('X = Y')


color = input('Color: ')
match color:
    case 'red' | 'no': print('STOP')
    case 'green': print('GO')
    case _: print(None)

"""
h
0 - 4 ночь
4 - 12 утро
12 - 17 день
17 - 24 вечер
"""
h = 4
if 4 <= h < 12:
    print('Утро')
